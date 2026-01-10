from rest_framework import serializers
from .models import Event, User, Post, Comment, Photo, EventFavorite, Repost


class UserSerializer(serializers.ModelSerializer):
    photo = serializers.SerializerMethodField()

@@ -26,12 +22,9 @@ def get_photo(self, obj):


class PhotoSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    
    class Meta:
        model = Photo
        fields = ['id', 'content_type', 'image', 'uploaded_at', 'event', 'post']
    
    def get_image(self, obj):
        if obj.image:
            url = obj.image.url
@@ -46,51 +39,8 @@ def get_image(self, obj):
        return None

class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    photos = PhotoSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = '__all__'


class EventSerializer(serializers.ModelSerializer):
    creator = UserSerializer(read_only=True)
    photos = PhotoSerializer(many=True, read_only=True)
    posts = PostSerializer(many=True, read_only=True)

    class Meta:
        model = Event
        fields = '__all__'


class EventFavoriteSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    event = EventSerializer(read_only=True)

    class Meta:
        model = EventFavorite
        fields = '__all__'


class RepostSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    event = EventSerializer(read_only=True)

    class Meta:
        model = Repost
        fields = ['id', 'user', 'event', 'caption', 'created_at']

