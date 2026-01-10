class UserSerializer(serializers.ModelSerializer):
    photo = serializers.SerializerMethodField()
    
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'name', 'lastname', 'photo')
    
    def get_photo(self, obj):
        if obj.photo:
            # Return full URL for Cloudinary or local storage
            if hasattr(obj.photo, 'url'):
                url = obj.photo.url
                # If it's a Cloudinary URL, it's already absolute
                if url.startswith('http'):
                    return url
                # For local storage, build absolute URI
                request = self.context.get('request')
                if request:
                    return request.build_absolute_uri(url)
                return url
        return None


class PhotoSerializer(serializers.ModelSerializer):
@@ -16,11 +33,16 @@ class Meta:
        fields = ['id', 'content_type', 'image', 'uploaded_at', 'event', 'post']

    def get_image(self, obj):
        if obj.image:
            url = obj.image.url
            # If it's a Cloudinary URL, it's already absolute
            if url.startswith('http'):
                return url
            # For local storage, build absolute URI
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(url)
            return url
        return None

class CommentSerializer(serializers.ModelSerializer):
@@ -69,4 +91,3 @@ class Meta:
        fields = ['id', 'user', 'event', 'caption', 'created_at']



