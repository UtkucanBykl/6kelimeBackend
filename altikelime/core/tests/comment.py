from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from ..models import Post, Category
from rest_framework.authtoken.models import Token
from django.urls import reverse_lazy

__all__ = ['CommentTestCase']


class CommentTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(username='hikmet', email='a@a.com')
        self.user.set_password('123456')
        self.user.save()
        self.category = Category.objects.create(name='Cat1')

    def test_comment_create(self):
        client = APIClient()
        token = Token.objects.get(user=self.user)
        post = Post.objects.create(user=self.user, content='utku is here my is not', category=self.category)
        client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        url = reverse_lazy('core:comment-create', kwargs={'slug': post.slug})
        data = {
            'comment': 'hello',
        }
        response = client.post(url, data, format='json')
        print(response)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_comment_create_with_empty_data(self):
        client = APIClient()
        token = Token.objects.get(user=self.user)
        post = Post.objects.create(user=self.user, content='utku is here my is not', category=self.category)
        client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        url = reverse_lazy('core:comment-create', kwargs={'slug': post.slug})
        data = {
            'comment': '',
        }
        response = client.post(url, data, format='json')
        print(response)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_comment_create_with_not_auth(self):
        client = APIClient()
        post = Post.objects.create(user=self.user, content='utku is here my is not', category=self.category)
        url = reverse_lazy('core:comment-create', kwargs={'slug': post.slug})
        data = {
            'comment': '',
        }
        response = client.post(url, data, format='json')
        print(response)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_comment_create_with_not_create_post(self):
        client = APIClient()
        token = Token.objects.get(user=self.user)
        client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        url = reverse_lazy('core:comment-create', kwargs={'slug': 'deneme'})
        data = {
            'comment': '',
        }
        response = client.post(url, data, format='json')
        print(response)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
