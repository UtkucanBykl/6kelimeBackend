from rest_framework import status
from rest_framework.authtoken.views import APIView
from rest_framework.response import Response
from django.contrib.auth import login as django_login, logout as django_logout
from rest_framework.authentication import TokenAuthentication
from ..serializers import LoginSerializer, UserDetailSerializer

__all__ = ['LoginView', 'LogoutView']


class LoginView(APIView):

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        django_login(request, user)

        return Response(
            UserDetailSerializer(user).data,
            status=status.HTTP_201_CREATED
        )


class LogoutView(APIView):
    
    authentication_classes = (TokenAuthentication,)

    def post(self, request):
        django_logout(request)
        return Response(status=status.HTTP_200_OK)
