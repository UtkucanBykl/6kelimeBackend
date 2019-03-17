from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny

from ..serializers import PostListSerializer
from ..models import Post


__all__ = ['CategoryPostsListView']


class CategoryPostsListView(ListAPIView):
    serializer_class = PostListSerializer
    queryset = Post.objects.actives().filter(publish=True)
    permission_classes = (AllowAny, )

    def get_queryset(self):
        qs = super(CategoryPostsListView, self).get_queryset()
        return qs.filter(category__name=self.kwargs['cat_name'])
