from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

__all__ = ['LoginSerializer', 'RegisterSerializer']


class LoginSerializer(serializers.Serializer):

    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):

        username = data.get('username', '')
        password = data.get('password', '')

        if username and password:
            user = authenticate(request=data, username=username, password=password)

            if not user:
                msg = 'Bu bilgiler ile giriş yapılamıyor'
                raise serializers.ValidationError(msg, code='authorization')
            else:
                data['user'] = user

        else:
            msg = 'Kullanıcı Adı ve Parola içermelidir.'
            raise serializers.ValidationError(msg, code='authorization')

        return data


class RegisterSerializer(serializers.ModelSerializer):

    class Meta:

        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')


