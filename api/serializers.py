from rest_framework import serializers

from photogalle.models import Gallery, Photo, Comment


class NestedCommentSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username", read_only=True)

    class Meta:
        model = Comment
        fields = [
            "id",
            "comment",
            "date_time",
            "username",
        ]


class PhotoSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username", read_only=True)
    comments = NestedCommentSerializer(many=True, read_only=True)
    image_thumbnail = serializers.ImageField(required=False)

    class Meta:
        model = Photo
        fields = [
            "id",
            "title",
            "description",
            "date_time",
            "pinned",
            "comments",
            "image",
            "image_thumbnail",
            "username",
        ]


class NestedPhotoSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username", read_only=True)
    image_thumbnail = serializers.ImageField()

    class Meta:
        model = Photo
        fields = [
            "id",
            "title",
            "description",
            "date_time",
            "pinned",
            "comments",
            "image",
            "image_thumbnail",
            "username",
        ]


class GallerySerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username", read_only=True)
    photos = NestedPhotoSerializer(many=True, read_only=True)

    class Meta:
        model = Gallery
        fields = [
            "id",
            "title",
            "description",
            "photos",
            "private",
            "date_time",
            "username",
        ]


class NewCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            "pk",
            "photo",
            "comment",
        ]
