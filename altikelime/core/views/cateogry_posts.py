from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import ListAPIView

from ..serializers import PostListSerializer
from ..models import Post


__all__ = ['CategoryPostsListView']


class CategoryPostsListView(ListAPIView):
    authentication_classes = (TokenAuthentication,)
    serializer_class = PostListSerializer
    queryset = Post.objects.actives().filter(publish=True)

    def get_queryset(self):
        print(self.request.user)
        qs = super(CategoryPostsListView, self).get_queryset()
        return qs.filter(category__name=self.kwargs['cat_name'])
