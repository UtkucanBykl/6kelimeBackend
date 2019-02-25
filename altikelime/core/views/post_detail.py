from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import Post
from ..serializers import PostListSerializer

__all__ = ['PostDetailApiView']


class PostDetailApiView(APIView):

    def get_object(self, slug):
        try:
            print(slug)
            print(Post.objects.all())
            post = Post.objects.get(slug=slug)
        except:
            raise Http404
        return post

    def get(self, request, slug, *args, **kwargs):
        post = self.get_object(slug)
        print(post)
        serializer = PostListSerializer(post)
        return Response(serializer.data, status=status.HTTP_200_OK)
