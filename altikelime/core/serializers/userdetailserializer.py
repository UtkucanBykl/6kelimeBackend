from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token

__all__ = ['UserDetailSerializer']


class UserDetailSerializer(serializers.ModelSerializer):

    class Meta:

        model = User
        fields = ('username', 'email')

