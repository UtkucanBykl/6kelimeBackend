from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.authtoken.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from django.contrib.auth import login as django_login, logout as django_logout
from rest_framework.authentication import TokenAuthentication
from ..serializers import LoginSerializer, LoginUserSerializer, RegisterSerializer

__all__ = ['LoginView', 'RegisterView', 'LogoutView']


class LoginView(APIView):

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        django_login(request, user)

        return Response(
            LoginUserSerializer(user).data,
            status=status.HTTP_200_OK
        )


class RegisterView(CreateAPIView):

    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.data
        user = User.objects.create(**data)
        user.set_password(serializer.data['password'])
        user.save()
        return Response(
            {'status': 'success'},
            status=status.HTTP_201_CREATED,
        )


class LogoutView(APIView):
    
    authentication_classes = (TokenAuthentication, )

    def post(self, request):
        django_logout(request)
        return Response(status=status.HTTP_200_OK)
