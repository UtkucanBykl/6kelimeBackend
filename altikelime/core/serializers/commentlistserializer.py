from rest_framework import serializers

from ..models import Comment
from ..serializers import UserDetailSerializer

__all__ = ['PostCommentListSerializer']


class PostCommentListSerializer(serializers.ModelSerializer):

    user = UserDetailSerializer()

    class Meta:
        model = Comment
        fields = ('user', 'post', 'publish', 'comment')
