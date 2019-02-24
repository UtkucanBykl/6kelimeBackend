from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from ..serializers import PostCreateSerializer

__all__ = ['PostCreateApiView']


class PostCreateApiView(CreateAPIView):

    serializer_class = PostCreateSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def create(self, request, *args, **kwargs):
        super(PostCreateApiView, self).create(request, *args, **kwargs)
        return Response(
            {'status': 'success'},
            status=status.HTTP_201_CREATED,
        )
