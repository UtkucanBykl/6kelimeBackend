from rest_framework import serializers


from ..models import Post

__all__ = ['PostCreateSerializer']


class PostCreateSerializer(serializers.ModelSerializer):

    user = serializers.JSONField(required=False)

    class Meta:

        model = Post
        fields = ('content', 'publish', 'category', 'user')

    def validate(self, data):

        content = data.get('content')
        words = content.split()

        if len(words) != 6:
            raise serializers.ValidationError('Gönderi 6 kelime değil')

        return data
