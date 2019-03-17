from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from ..serializers import CommentCreateSerializer

from ..models import Post

__all__ = ['CommentCreateApiView']


class CommentCreateApiView(CreateAPIView):

    permission_classes = (IsAuthenticated,)
    serializer_class = CommentCreateSerializer

    def perform_create(self, serializer, *args, **kwargs):
        serializer.save(user=self.request.user, post=kwargs['post'])

    def create(self, request, *args, **kwargs):
        try:
            post = Post.objects.get(slug=kwargs['slug'])
        except:
            return Response(
                {'status': 'Böyle bir post yok'},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            kwargs['post'] = post
            self.perform_create(serializer, *args, **kwargs)
        return Response(
            {'status': 'success'},
            status=status.HTTP_201_CREATED
        )
