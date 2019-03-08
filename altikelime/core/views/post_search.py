from rest_framework.generics import ListAPIView

from ..serializers import PostListSerializer
from ..models import Post

__all__ = ['PostSearchListAPIView']


class PostSearchListAPIView(ListAPIView):

    serializer_class = PostListSerializer
    queryset = Post.objects.actives()

    def get_queryset(self):
        qs = super(PostSearchListAPIView, self).get_queryset()
        content = self.request.GET.get('content', '')
        username = self.request.GET.get('username', '')
        qs = qs.filter(user__username__icontains=username, content__icontains=content)
        return qs
