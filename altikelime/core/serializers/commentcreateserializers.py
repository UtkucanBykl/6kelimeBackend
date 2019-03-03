from rest_framework import serializers
from ..models import Comment

__all__ = ["CommentCreateSerializer"]


class CommentCreateSerializer(serializers.ModelSerializer):
    print(serializers)

    class Meta:
        model = Comment
        fields = ('comment', )
