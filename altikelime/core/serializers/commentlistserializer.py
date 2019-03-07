from rest_framework import serializers

from ..models import Comment

__all__ = ['PostCommentListSerializer']


class PostCommentListSerializer(serializers.ModelSerializer):

    user= serializers.JSONField()

    class Meta:
        model = Comment
        fields = ('user', 'post', 'publish', 'comment')
