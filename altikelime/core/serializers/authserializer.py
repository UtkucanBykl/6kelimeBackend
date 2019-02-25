from rest_framework import serializers
from django.contrib.auth import authenticate

__all__ = ['LoginSerializer']


class LoginSerializer(serializers.Serializer):

    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):

        username = data.get('username', '')
        password = data.get('password', '')

        if username and password :
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


