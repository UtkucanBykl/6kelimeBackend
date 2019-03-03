from rest_framework import serializers
from ..models import Comment
from ..serializers import UserDetailSerializer

__all__ = ["CommentCreateSerializer"]


class CommentCreateSerializer(serializers.ModelSerializer):

    user = serializers.JSONField(required=False)

    class Meta:
        model = Comment
        fields = ('user', 'publish', 'post', 'comment', )
