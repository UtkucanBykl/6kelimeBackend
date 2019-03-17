from rest_framework import status
from rest_framework.generics import DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from ..models import Post
from ..permissions import  IsOwner

__all__ = ['PostDeleteApiView']


class PostDeleteApiView(DestroyAPIView):
    permission_classes = (IsAuthenticated, IsOwner)
    lookup_field = 'slug'
    lookup_url_kwarg = 'slug'
    queryset = Post.objects.actives()

    def get_queryset(self):
        qs = super(PostDeleteApiView, self).get_queryset()
        qs = qs.filter(user=self.request.user)
        return qs

    def destroy(self, request, *args, **kwargs):
        super(PostDeleteApiView, self).destroy(request, *args, **kwargs)
        return Response({'status': 'success'}, status=status.HTTP_200_OK)
