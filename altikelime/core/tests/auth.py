from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.urls import reverse_lazy
import json

class AuthTestCase(APITestCase):

    def setUp(self):

        self.user = User.objects.create_user(username="hikmet", email="a@a.com")
        self.user.set_password('123456')
        self.user.save()
        Token.objects.create(user=self.user)

    def test_login(self):

        token = Token.objects.get(user__username='hikmet')
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        url = reverse_lazy("core:login")
        data = {'username': 'hikmet', 'password': '123456'}
        response = client.post(url, data, format='json')
        raw_data = response.content.decode("utf-8")
        raw_data = json.loads(raw_data)
        self.assertEqual(str(token.key), raw_data["token"])
