from django.contrib.auth.models import User
from django.urls import reverse_lazy
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase, APIClient

from ..models import Category, Post
from ..serializers import PostListSerializer


class PostTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(username='utkucan', email='1234@dd.com')
        self.user.set_password('123456')
        self.user.save()
        Token.objects.create(user=self.user)
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
