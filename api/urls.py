from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

api_router = DefaultRouter()
api_router.register("galleries", viewset=views.GalleryViewSet, basename="gallery")
api_router.register("photos", viewset=views.PhotoViewSet, basename="photo")

urlpatterns = api_router.urls


# urlpatterns = [
#     path("gallery_list/", views.GalleryList.as_view()),
#     path("gallery_list/<int:pk>", views.GalleryDetail.as_view()),
#     path("photo_list/", views.PhotoList.as_view()),
#     path("photo_detail/", views.PhotoDetail.as_view()),
# ]
