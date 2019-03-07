from rest_framework import serializers

from ..serializers import UserDetailSerializer
from ..models import Like

__all__ = ['LikeListSerializer']


class LikeListSerializer(serializers.ModelSerializer):

    user = UserDetailSerializer()

    class Meta:
        model = Like
        fields = ('user', 'update_at')
