from photogalle.models import Gallery, Photo, Comment
from api.serializers import GallerySerializer, PhotoSerializer, NestedCommentSerializer
from rest_framework import generics, viewsets


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