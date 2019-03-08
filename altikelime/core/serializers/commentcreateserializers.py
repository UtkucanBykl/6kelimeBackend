from rest_framework import serializers
from ..models import Comment

__all__ = ["CommentCreateSerializer"]


class CommentCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('comment', )
