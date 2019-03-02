from rest_framework.generics import ListAPIView

from ..serializers import PostListSerializer
from ..models import Post

__all__ = ['MostLikeListView']


class MostLikeListView(ListAPIView):
    serializer_class = PostListSerializer
    queryset = Post.objects.actives().filter(publish=True)

    def get_queryset(self):
        qs = super(MostLikeListView, self).get_queryset()
        data = sorted(qs, key=lambda x: x.like_count)[::-1]
        return data
