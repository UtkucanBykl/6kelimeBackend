from django.contrib.auth.models import User
from rest_framework import serializers

__all__ = ['UserDetailSerializer']


class UserDetailSerializer(serializers.ModelSerializer):

    class Meta:

        model = User
        fields = ('username', 'email')

