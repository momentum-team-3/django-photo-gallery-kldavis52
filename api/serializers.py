from rest_framework import serializers

from photogalle.models import Gallery, Photo, Comment


class GallerySerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username", read_only=True)

    class Meta:
        model = Gallery
        fields = [
            "id",
            "title",
            "description",
            "private",
            "date_time",
            "username",
        ]


class PhotoSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username", read_only=True)

    class Meta:
        model = Photo
        fields = [
            "id",
            "title",
            "description",
            "date_time",
            "pinned",
            "username",
        ]


class CommentSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username", read_only=True)

    class Meta:
        model = Comment
        fields = [
            "id",
            "comment",
            "date_time",
            "username",
        ]
