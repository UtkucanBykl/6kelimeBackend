from rest_framework.generics import DestroyAPIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from ..models import Comment, Post

__all__ = ["CommentDeleteApiView"]


class CommentDeleteApiView(DestroyAPIView):

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Comment.objects.actives()
    lookup_field = 'slug'
    lookup_url_kwarg = 'slug'

    def get_queryset(self):
        qs = super(CommentDeleteApiView, self).get_queryset()
        qs = qs.filter(user=self.request.user)
        return qs

    def destroy(self, request, *args, **kwargs):
        slug = self.kwargs['slug']
        try:
            Post.objects.get(slug=slug)
        except:
            return Response({'status': 'Böyle bir post yok'},
                            status=status.HTTP_404_NOT_FOUND
                            )
        super(CommentDeleteApiView, self).delete(request,*args,**kwargs)
        return Response({'status': 'success'},
                        status=status.HTTP_204_NO_CONTENT
                        )
