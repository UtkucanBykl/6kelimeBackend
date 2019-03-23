from rest_framework import serializers

from ..models import Like, Post
from ..serializers import UserDetailSerializer

__all__ = ['PostListSerializer']


class PostListSerializer(serializers.ModelSerializer):

    user = UserDetailSerializer()
    category_name = serializers.SerializerMethodField()
    is_like = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = (
            'user',
            'content',
            'category_name',
            'update_at',
            'publish',
            'is_like',
            'like_count',
            'slug',
        )

    def get_category_name(self, obj):
        return obj.category.name

    def get_is_like(self, obj):
        request = self.context.get('request', None)
        if not request or not request.user.is_authenticated:
            return False
        return Like.objects.filter(post=obj, user=self.context['request'].user).exists()
