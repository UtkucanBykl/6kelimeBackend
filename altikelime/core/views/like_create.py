from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from ..models import Like, Post

__all__ = ['LikeCreateOrDeleteView']


class LikeCreateOrDeleteView(CreateAPIView):
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )
    queryset = Like.objects.all()

    def create(self, request, *args, **kwargs):
        try:
            post = Post.objects.get(slug=kwargs['slug'])
        except:
            return Response({'status': 'Böyle Bir Gönderi Yok'}, status=status.HTTP_404_NOT_FOUND)
        user = self.request.user
        qs = self.get_queryset()
        if qs.filter(user=user, post=post).exists():
            qs.filter(user=user, post=post).delete()
            return Response({'status': 'created'}, status=status.HTTP_201_CREATED)
        else:
            Like.objects.create(user=user, post=post)
            return Response({'status': 'deleted'}, status=status.HTTP_201_CREATED)
