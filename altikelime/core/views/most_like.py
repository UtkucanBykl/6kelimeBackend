from django.db.models import Count, F
from rest_framework.generics import ListAPIView

from ..models import Post
from ..serializers import PostListSerializer

__all__ = ['MostLikeListView']


class MostLikeListView(ListAPIView):
    serializer_class = PostListSerializer
    queryset = Post.objects.actives().filter(publish=True)

    def get_queryset(self):
        qs = super(MostLikeListView, self).get_queryset()
        qs = (
            qs.select_related('category', 'user')
            .annotate(likeeee=Count('likes'))
            .order_by('-likeeee')
        )
        return qs
