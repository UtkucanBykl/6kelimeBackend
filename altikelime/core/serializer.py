from rest_framework import serializers
from core.models import Post

class PostSerializers(serializers.ModelSerializer):

    content = serializers.CharField()
    publish = serializers.BooleanField()

    class Meta:
        model = Post
        fields = ("content", "publish", )

    def validate(self, data):
        space = 0
        content = data.get("content")
        
        for line in content: 
            if (line.isspace()) == True: 
                space+=1

        if space != 6 :
            raise serializers.ValidationError("Post 6 kelime değil")
        
        return data
        
        