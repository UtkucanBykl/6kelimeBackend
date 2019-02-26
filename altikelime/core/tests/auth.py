import json

from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.urls import reverse_lazy


__all__ = ['AuthTestCase']


class AuthTestCase(APITestCase):

    def setUp(self):

        self.user = User.objects.create(username="hikmet", email="a@a.com")
        self.user.set_password('123456')
        self.user.save()

    def test_login(self):

        token = Token.objects.get(user__username='hikmet')
        client = APIClient()
        url = reverse_lazy("core:login")
        data = {'username': 'hikmet', 'password': '123456'}
        response = client.post(url, data, format='json')
        raw_data = response.content.decode("utf-8")
        raw_data = json.loads(raw_data)
        self.assertEqual(str(token.key), raw_data["token"])

    def test_register(self):

        client = APIClient()
        url = reverse_lazy("core:register")
        data = {
            'username': 'hikmos',
            'first_name': 'hikmet',
            'last_name': 'semiz',
            'email': 'a@a.com',
            'password': '123456',
        }
        response = client.post(url, data, format='json')
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
