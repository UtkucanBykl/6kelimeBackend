from rest_framework.generics import UpdateAPIView
from rest_framework.response import Response

from ..models import Post
from ..permissions import IsOwner
from ..serializers import PostCreateSerializer

__all__ = ['PostUpdateAPIView']


class PostUpdateAPIView(UpdateAPIView):
    allowed_methods = ['PUT', 'PATCH']
    serializer_class = PostCreateSerializer
    permission_classes = (IsOwner,)
    lookup_field = 'slug'
    lookup_url_kwarg = 'slug'
    queryset = Post.objects.actives().select_related('category')

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

    def update(self, request, *args, **kwargs):
        super(PostUpdateAPIView, self).update(request, *args, **kwargs)
        return Response({'status': 'success'})
