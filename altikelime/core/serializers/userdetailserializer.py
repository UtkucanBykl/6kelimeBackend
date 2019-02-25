from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token

__all__ = ['UserDetailSerializer']


class UserDetailSerializer(serializers.ModelSerializer):

    token = serializers.SerializerMethodField()

    class Meta:

        model = User
        fields = ('token', 'username', 'email')

    def get_token(self, obj):
        return Token.objects.get(user=obj).key
