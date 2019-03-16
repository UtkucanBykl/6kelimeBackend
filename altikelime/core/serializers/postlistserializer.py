from rest_framework import serializers

from ..serializers import UserDetailSerializer
from ..models import Post, Like

__all__ = ['PostListSerializer']


class PostListSerializer(serializers.ModelSerializer):

    user = UserDetailSerializer()
    category_name = serializers.SerializerMethodField()
    is_like = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ('user', 'content', 'category_name', 'update_at', 'publish', 'is_like')

    def get_category_name(self, obj):
        return obj.category.name

    def get_is_like(self, obj):
        return False