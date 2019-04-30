from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from ..models import Post
from ..serializers import PostListSerializer

__all__ = ['PostUnpublishListAPIView']


class PostUnpublishListAPIView(ListAPIView):
    serializer_class = PostListSerializer
    queryset = Post.objects.filter(publish=False)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        qs = super(PostUnpublishListAPIView, self).get_queryset()
        return qs.filter(user=self.request.user).select_related('category')
