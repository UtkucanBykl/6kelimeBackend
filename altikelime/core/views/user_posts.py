from django.db.models import BooleanField, Case, Count, F, Value, When
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from ..models import Post
from ..serializers import PostListSerializer

__all__ = ['UserPostListView']


class UserPostListView(ListAPIView):

    serializer_class = PostListSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Post.objects.actives().select_related('category')

    def get_queryset(self):
        qs = super(UserPostListView, self).get_queryset()
        qs = (
            qs.filter(user=self.request.user)
            .annotate(like_list=F('likes'))
            .annotate(
                is_likee=Case(
                    When(user__in=F('like_list'), then=Value(True)),
                    default=Value(False),
                    output_field=BooleanField(),
                )
            )
        )
        print(qs.first().is_likee)
        return qs
