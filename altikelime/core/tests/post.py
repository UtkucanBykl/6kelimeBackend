from django.contrib.auth.models import User
from django.urls import reverse_lazy
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase, APIClient

from core.models import Category


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
