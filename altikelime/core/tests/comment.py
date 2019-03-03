import json

from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from ..models import Post, Category, Comment
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
            'user': self.user.id,
            'post': post.id,
        }
        response = client.post(url, data, format='json')
        print(response)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
