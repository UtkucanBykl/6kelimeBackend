from rest_framework import serializers

from ..serializers import UserDetailSerializer
from ..models import Post

__all__ = ['PostListSerializer']


class PostListSerializer(serializers.ModelSerializer):

    user = UserDetailSerializer()
    category_name = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ('user', 'content', 'category_name', 'update_at', 'publish')

    def get_category_name(self, obj):
        return obj.category.name
