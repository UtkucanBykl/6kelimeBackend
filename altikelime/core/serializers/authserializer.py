from rest_framework import serializers
from django.contrib.auth import authenticate


class LoginSerializers(serializers.Serializer):

    username = serializers.CharField(label="Kullanıcı Adı")
    password = serializers.CharField(
        label="Parola",
        style={'input_type': 'password'},
        trim_whitespace=False
    )

    def validate(self, data):

        username = data.get("username", "")
        password = data.get("password", "")

        if username and password :
            user = authenticate(request=data, username=username, password=password)

            if not user:
                msg = 'Bu bilgiler ile giriş yapılamıyor'
                raise serializers.ValidationError(msg, code="authorization")
            else:
                data['user'] = user

        else:
            msg = "Kullanıcı Adı ve Parola içermelidir."
            raise serializers.ValidationError(msg, code="authorization")

        return data


