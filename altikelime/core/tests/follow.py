from django.contrib.auth.models import User
from django.urls import reverse_lazy
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient, APITestCase

__all__ = ['FollowTestCase']


class FollowTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username='utkucan', email='1234@dd.com')
        self.user.set_password('123456')
        self.user.save()

        self.user2 = User.objects.create(username='ahmet', email='ahmet@dd.com')
        self.user2.set_password('123456')
        self.user2.save()

    def test_follow_create(self):
        client = APIClient()
        token = Token.objects.get(user=self.user)
        client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        data = {
            'following': self.user2.username
        }
        url = reverse_lazy('core:follow-create')
        response = client.post(url, data)
        self.assertEqual(response.status_code, 201)
