from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from ..serializers import PostListSerializer
from ..models import Post

__all__ = ['UserPostListView']


class UserPostListView(ListAPIView):

    serializer_class = PostListSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )
    queryset = Post.objects.actives().select_related('category')

    def get_queryset(self):
        qs = super(UserPostListView, self).get_queryset()
        qs = qs.filter(user=self.request.user)
        return qs
