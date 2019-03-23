from django.contrib.auth.models import User
from django.urls import reverse_lazy
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient, APITestCase

from ..models import Category, Like, Post
from ..serializers import (LikeListSerializer, PostDetailSerializer,
                           PostListSerializer)

__all__ = ['PostTestCase']


class PostTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(username='utkucan', email='1234@dd.com')
        self.user.set_password('123456')
        self.user.save()
        self.category = Category.objects.create(name='Cat1')

    def test_create_post_with_correct_data(self):
        client = APIClient()
        token = Token.objects.get(user=self.user)
        client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        url = reverse_lazy('core:post-create')
        category = Category.objects.all().first()
        post_data = {
            'content': '1 2 3 4 5 6',
            'category': category.id
        }
        response = client.post(url, post_data, format='json')
        self.assertEquals(response.data['status'], 'success')

    def test_get_user_posts(self):
        client = APIClient()
        token = Token.objects.get(user=self.user)
        Post.objects.create(user=self.user, content="1 2 3 4 5 6", category=self.category)
        client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        url = reverse_lazy('core:post-user')
        serializer = PostListSerializer(Post.objects.filter(user=self.user), many=True)
        response = client.get(url)
        self.assertEquals(serializer.data, response.data)

    def test_get_post_detaill(self):
        client = APIClient()
        post = Post.objects.create(user=self.user, content="1 2 3 4 5 6", category=self.category)
        url = reverse_lazy('core:post-detail', kwargs={'slug': post.slug})
        Like.objects.create(user=self.user, post=post)
        response = client.get(url)
        serializer = PostDetailSerializer(post, many=False)
        self.assertEquals(response.data, serializer.data)

    def test_get_category_posts(self):
        client = APIClient()
        Post.objects.create(user=self.user, content="1 2 3 4 5 6", category=self.category)
        Post.objects.create(user=self.user, content="1 2 3 4 5 6", category=self.category)
        url = reverse_lazy('core:post-category', kwargs={'cat_name': self.category.name})
        response = client.get(url)
        serializer = PostListSerializer(Post.objects.filter(category=self.category), many=True)
        self.assertEquals(response.data, serializer.data)

    def test_create_like(self):
        client = APIClient()
        token = Token.objects.get(user=self.user)
        post = Post.objects.create(user=self.user, content="1 2 3 4 5 6", category=self.category)
        client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        url = reverse_lazy('core:like-create', kwargs={'slug': post.slug})
        response = client.post(url)
        self.assertEquals(Post.objects.get(id=post.id).like_count, 1)
        self.assertEquals(response.status_code, 201)
        client.post(url)
        self.assertEquals(Post.objects.get(id=post.id).like_count, 0)

    def test_get_post_order_by_likes(self):
        client = APIClient()
        post = Post.objects.create(user=self.user, content="1 2 3 4 5 6", category=self.category)
        post3 = Post.objects.create(user=self.user, content="1 2 3 4 5 8", category=self.category)
        Post.objects.create(user=self.user, content="1 2 3 4 5 7", category=self.category)
        Like.objects.create(post=post, user=self.user)
        Like.objects.create(post=post3, user=self.user)
        url = reverse_lazy('core:most-like')
        response = client.get(url)
        data = sorted(Post.objects.filter(publish=True), key=lambda x: x.like_count)[::-1]
        serializer = PostListSerializer(data, many=True)
        self.assertEquals(response.data, serializer.data)

    def test_delete_post_with_correct(self):
        client = APIClient()
        post = Post.objects.create(user=self.user, content="1 2 3 4 5 6", category=self.category)
        url = reverse_lazy('core:post-delete', kwargs={'slug': post.slug})
        token = Token.objects.get(user=self.user)
        client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        response = client.delete(url)
        self.assertEquals(response.data, {'status': 'success'})
        self.assertEquals(Post.objects.filter(user=self.user).count(), 0)

    def test_delete_post_with_incorrect(self):
        user = User.objects.create(username='utq', email='1234@dd.com')
        user.set_password('123456')
        user.save()
        client = APIClient()
        post = Post.objects.create(user=user, content="1 2 3 4 5 6", category=self.category)
        Post.objects.create(user=self.user, content="1 2 3 4 5 6", category=self.category)
        url = reverse_lazy('core:post-delete', kwargs={'slug': post.slug})
        token = Token.objects.get(user=self.user)
        client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        response = client.delete(url)
        self.assertNotEqual(response.data, {'status': 'success'})

    def test_retrive_close_post_witH_incorrect_user(self):
        user = User.objects.create(username='utq', email='1234@dd.com')
        user.set_password('123456')
        user.save()
        client = APIClient()
        post = Post.objects.create(user=user, content="1 2 3 4 5 6", category=self.category)
        url = reverse_lazy('core:post-detail', kwargs={'slug': post.slug})
        token = Token.objects.get(user=self.user)
        client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        response = client.delete(url)
        serializer = PostDetailSerializer(post, many=False)
        self.assertNotEqual(response.data, serializer.data)

    def test_get_user_unpublish_post(self):
        client = APIClient()
        Post.objects.create(user=self.user, content="1 2 3 4 5 6", category=self.category, publish=False)
        Post.objects.create(user=self.user, content="1 2 3 4 5 7", category=self.category, publish=True)
        url = reverse_lazy('core:post-list-unpublish')
        token = Token.objects.get(user=self.user)
        client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        response = client.get(url)
        serializer = PostListSerializer(Post.objects.filter(publish=False, user=self.user), many=True)
        self.assertEquals(response.data, serializer.data)

    def test_get_post_like(self):
        client = APIClient()
        post = Post.objects.create(user=self.user, content="1 2 3 4 5 6", category=self.category)
        Like.objects.create(post=post, user=self.user)
        url = reverse_lazy('core:like-list', kwargs={'slug': post.slug})
        response = client.get(url)
        serializer = LikeListSerializer(Like.objects.filter(user=self.user, post=post), many=True)
        self.assertEquals(response.data, serializer.data)

    def test_get_post_like_with_raise(self):
        client = APIClient()
        post = Post.objects.create(user=self.user, content="1 2 3 4 5 6", category=self.category)
        Like.objects.create(post=post, user=self.user)
        url = reverse_lazy('core:like-list', kwargs={'slug': '1231231231231231231'})
        response = client.get(url)
        self.assertEquals(response.status_code, 404)

    def test_search_post_with_content_query(self):
        client = APIClient()
        Post.objects.create(user=self.user, content="1 2 3 4 5 6", category=self.category)
        base_url = reverse_lazy('core:post-search')
        search_url = f'{base_url}?content=1%202%203'
        response = client.get(search_url)
        serializer = PostListSerializer(Post.objects.actives().filter(content__icontains='1 2 3'), many=True)
        self.assertEqual(response.data, serializer.data)

    def test_search_post_with_content_and_username(self):
        client = APIClient()
        post = Post.objects.create(user=self.user, content="1 2 3 4 5 6", category=self.category)
        base_url = reverse_lazy('core:post-search')
        search_url = f'{base_url}?content=1%202%203&username=utkucan'
        response = client.get(search_url)
        serializer = PostListSerializer(Post.objects.actives().filter(content__icontains='1 2 3'), many=True)
        self.assertEqual(response.data, serializer.data)

    def test_patch_update(self):
        client = APIClient()
        token = Token.objects.get(user=self.user)
        post = Post.objects.create(user=self.user, content="1 2 3 4 5 6", category=self.category)
        client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        url = reverse_lazy('core:post-update', kwargs={'slug': post.slug})
        data = {
            'content': '1 2 3 4 5 5'
        }
        response = client.patch(url, data)
        self.assertEqual(response.data, {'status': 'success'})

    def test_put_update(self):
        client = APIClient()
        token = Token.objects.get(user=self.user)
        post = Post.objects.create(user=self.user, content="1 2 3 4 5 6", category=self.category)
        client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        url = reverse_lazy('core:post-update', kwargs={'slug': post.slug})
        data = {
            'content': '1 2 3 4 5 5',
            'category': self.category.id
        }
        response = client.put(url, data)
        self.assertEqual(response.data, {'status': 'success'})

    def test_patch_with_another_user(self):
        user = User.objects.create(username='utq', email='1234@dd.com')
        user.set_password('123456')
        user.save()
        client = APIClient()
        token = Token.objects.get(user=user)
        post = Post.objects.create(user=self.user, content="1 2 3 4 5 6", category=self.category)
        client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        url = reverse_lazy('core:post-update', kwargs={'slug': post.slug})
        data = {
            'content': '1 2 3 4 5 5'
        }
        response = client.patch(url, data)
        self.assertNotEqual(response.data, {'status': 'success'})     
