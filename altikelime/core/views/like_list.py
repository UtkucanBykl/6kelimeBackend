from django.http import Http404
from rest_framework.generics import ListAPIView

from ..models import Post
from ..serializers import LikeListSerializer

__all__ = ['LikeListAPIView']


class LikeListAPIView(ListAPIView):

    serializer_class = LikeListSerializer
    queryset = Post.objects.actives()

    def get_queryset(self):
        qs = super(LikeListAPIView, self).get_queryset()
        try:
            post = qs.get(slug=self.kwargs['slug'])
            return post.likes.actives()
        except Post.DoesNotExist as e:
            raise Http404("Post does not exist " + str(e))
