from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token

__all__ = ['LoginUserSerializer']


class LoginUserSerializer(serializers.ModelSerializer):

    token = serializers.SerializerMethodField()

    class Meta:

        model = User
        fields = ('username', 'email', 'token')

    def get_token(self, obj):
        return Token.objects.get(user=obj).key
