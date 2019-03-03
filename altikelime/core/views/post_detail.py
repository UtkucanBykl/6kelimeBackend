
from rest_framework.generics import RetrieveAPIView


from ..permissions import IsOwnerOrOpen
from ..models import Post
from ..serializers import PostListSerializer

__all__ = ['PostDetailApiView']


class PostDetailApiView(RetrieveAPIView):

    serializer_class = PostListSerializer
    lookup_url_kwarg = 'slug'
    lookup_field = 'slug'
    queryset = Post.objects.all()
    permission_classes = (IsOwnerOrOpen, )
