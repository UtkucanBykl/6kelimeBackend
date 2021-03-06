from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from ..models import Comment, Post
from ..serializers import PostCommentListSerializer

__all__ = ['PostCommentListApiView']


class PostCommentListApiView(ListAPIView):

    serializer_class = PostCommentListSerializer
    queryset = Comment.objects.actives().select_related('post', 'user')

    def get_queryset(self):
        slug = self.kwargs['slug']
        try:
            self.post = Post.objects.get(slug=slug)
        except:
            return Response(
                {'status': 'Böyle bir post yok'}, status=status.HTTP_404_NOT_FOUND
            )

        comment = super(PostCommentListApiView, self).get_queryset()
        comment = comment.filter(post=self.post)
        return comment
