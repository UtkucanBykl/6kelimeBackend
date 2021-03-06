
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.urls import reverse_lazy


__all__ = ['AuthTestCase']


class AuthTestCase(APITestCase):

    def setUp(self):

        self.user = User.objects.create(username='hikmet', email='a@a.com')
        self.user.set_password('123456')
        self.user.save()

    def test_login(self):

        token = Token.objects.get(user__username='hikmet')
        client = APIClient()
        url = reverse_lazy('core:login')
        data = {'username': 'hikmet', 'password': '123456'}
        response = client.post(url, data, format='json')
        self.assertEqual(str(token.key), response.data['token'])

    def test_login_with_incorrect_data(self):
        client = APIClient()
        url = reverse_lazy('core:login')
        data = {'username': 'hikmet', 'password': '12332131456'}
        response = client.post(url, data, format='json')
        self.assertRaisesMessage(response.data, 'Bu bilgiler ile giriş yapılamıyor')

    def test_login_with_empty_data(self):
        client = APIClient()
        url = reverse_lazy('core:login')
        data = {'username': 'hikmet'}
        response = client.post(url, data, format='json')
        self.assertRaisesMessage(response.data, 'Kullanıcı Adı ve Parola içermelidir.')

    def test_register(self):

        client = APIClient()
        url = reverse_lazy('core:register')
        data = {
            'username': 'hikmos',
            'first_name': 'hikmet',
            'last_name': 'semiz',
            'email': 'a@a.com',
            'password': '123456',
        }
        response = client.post(url, data, format='json')
        self.assertEquals(User.objects.filter(username='hikmos').count(), 1)
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
