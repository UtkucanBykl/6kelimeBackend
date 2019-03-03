from rest_framework.generics import CreateAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from ..serializers import CommentCreateSerializer

from ..models import Post,Comment

__all__ = ['CommentCreateApiView']


class CommentCreateApiView(CreateAPIView):

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = CommentCreateSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def create(self, request, *args, **kwargs):
        post = Post.objects.get(slug=kwargs['slug'])
        if post:
            super(CommentCreateApiView, self).create(request, *args, **kwargs)
            return Response(
                {'status': 'success'},
                status=status.HTTP_201_CREATED
            )
        else:
            return Response({'status': 'Böyle Bir Gönderi Yok'}, status=status.HTTP_404_NOT_FOUND)
