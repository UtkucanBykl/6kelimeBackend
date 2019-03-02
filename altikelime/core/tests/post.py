from django.contrib.auth.models import User
from django.urls import reverse_lazy
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase, APIClient

from ..models import Category, Post, Like
from ..serializers import PostListSerializer


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
        print(response.data)
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
        response = client.get(url)
        serializer = PostListSerializer(post, many=False)
        self.assertEquals(response.data, serializer.data)

    def test_get_category_posts(self):
        client = APIClient()
        Post.objects.create(user=self.user, content="1 2 3 4 5 6", category=self.category)
        Post.objects.create(user=self.user, content="1 2 3 4 5 6", category=self.category)
        url = reverse_lazy('core:post-category', kwargs={'cat_name': self.category.name})
        response = client.get(url)
        serializer = PostListSerializer(Post.objects.filter(category=self.category), many=True)
        print(response.data)
        print(serializer.data)
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
        print(response.data)
        self.assertNotEqual(response.data, {'status': 'success'})
