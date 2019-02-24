from rest_framework import serializers


from ..models import Post

__all__ = ['PostSerializers']


class PostSerializers(serializers.ModelSerializer):

    class Meta:

        model = Post
        fields = ("content", "publish",)

    def validate(self, data):

        content = data.get("content")
        words = content.split()

        if len(words) != 6:
            raise serializers.ValidationError("Gönderi 6 kelime değil")

        return data
