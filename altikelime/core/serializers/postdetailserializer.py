from rest_framework import serializers

from ..serializers import UserDetailSerializer, LikeListSerializer
from ..models import Post

__all__ = ['PostDetailSerializer']


class PostDetailSerializer(serializers.ModelSerializer):
    likes = LikeListSerializer(many=True)
    user = UserDetailSerializer()
    category_name = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ('user', 'content', 'category_name', 'update_at', 'publish', 'likes')

    def get_category_name(self, obj):
        return obj.category.name