from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import ListAPIView

from ..models import Post
from ..serializers import PostListSerializer

__all__ = ['CategoryPostsListView']


class CategoryPostsListView(ListAPIView):
    authentication_classes = (TokenAuthentication,)
    serializer_class = PostListSerializer
    queryset = Post.objects.actives().filter(publish=True)

    def get_queryset(self):
        qs = super(CategoryPostsListView, self).get_queryset()
        return qs.filter(category__name=self.kwargs['cat_name'])
