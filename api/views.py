from rest_framework import viewsets, views, generics, status
from rest_framework.parsers import (
    FileUploadParser,
    ParseError,
    MultiPartParser,
    FormParser,
)
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied

from photogalle.models import Gallery, Photo, Comment
from api.serializers import (
    GallerySerializer,
    PhotoSerializer,
    NestedCommentSerializer,
    NewCommentSerializer,
)


class GalleryViewSet(viewsets.ModelViewSet):
    serializer_class = GallerySerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        if self.action in [
            "list",
            "create",
            "retrieve",
        ]:
            return Gallery.objects.all()
        return self.request.user.galleries


class PhotoViewSet(viewsets.ModelViewSet):
    serializer_class = PhotoSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        if self.action in [
            "list",
            "create",
            "retrieve",
        ]:
            return Photo.objects.all()
        return self.request.user.photos


class ImageUploadView(views.APIView):
    parser_classes = [
        MultiPartParser,
        FormParser,
    ]

    def post(self, request, pk, format=None):
        print(request.data)
        serializer = PhotoSerializer(data=request.data)
        gallery = get_object_or_404(request.user.galleries, pk=pk)
        if serializer.is_valid():
            photo = serializer.save(user=request.user)
            serializer.save()
            gallery.photo.add(photo)
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def post(self, request, pk):
    #     photo_serializer = PhotoSerializer(data=request.data)
    #     gallery = get_object_or_404(self.request.user.galleries, pk=pk)
    #     # Read the uploaded file
    #     if photo_serializer.is_valid():
    #         photo = photo_serializer.save(user=self.request.user)
    #         gallery.photo.add(photo)
    #         return Response(data=photo_serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(
    #         data=photo_serializer.error_messages, status=status.HTTP_400_BAD_REQUEST
    #     )

    # if "file" not in request.data:
    #     raise ParseError("Empty content")

    # file = request.data["file"]
    # gallery.photo.save(file.name, file, save=True)
    # return Response(status=status.HTTP_201_CREATED)


# class CommentViewSet(viewsets.ModelViewSet):
#     serializer_class = CommentSerializer

#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)

#     def get_queryset(self):
#         if self.action in [
#             "list",
#             "create",
#             "retrieve",
#         ]:
#             return Comment.objects.all()
#         return self.request.user.comments


# class CommentCreateView(generics.CreateAPIView):
#     serializer_class = NewCommentSerializer
#     queryset = Photo.objects.all()

#     def perform_create(self, serializer):
#         serializer.is_valid()
#         comment = serializer.validated_data["recipe"]
#         if self.request.user != recipe.user:
#             raise PermissionDenied("You are not the owner of that recipe")
#         serializer.save()


# class CommentViewSet(viewsets.ModelViewSet):
#     serializer_class = CommentSerializer

#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)

#     def get_queryset(self):
#         if self.action in [
#             "list",
#             "create",
#             "retrieve",
#         ]:
#             return Comment.objects.all()
#         return self.request.user.comments


# class GalleryList(generics.ListCreateAPIView):
#     serializer_class = GallerySerializer

#     def get_queryset(self):
#         return Gallery.objects.for_user(self.request.user)

#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)


# class GalleryDetail(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = GallerySerializer

#     def get_queryset(self):
#         return self.request.user.galleries


# class PhotoList(generics.ListCreateAPIView):
#     queryset = Photo.objects.all()
#     serializer_class = PhotoSerializer


# class PhotoDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Photo.objects.all()
#     serializer_class = PhotoSerializer


# class CommentList(generics.ListCreateAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer


# class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer