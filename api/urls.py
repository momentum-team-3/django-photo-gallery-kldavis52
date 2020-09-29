from django.urls import path

from . import views

# from rest_framework.routers import DefaultRouter

# api_router = DefaultRouter()
# api_router.register("galleries", viewset=views.GalleryViewSet, basename="gallery")
# api_router.register(
#     "galleries/<int:pk>", viewset=views.GalleryViewSet, basename="gallery_detail"
# )
# api_router.register(
#     "galleries/<int:pk>/photos", viewset=views.PhotoViewSet, basename="photo"
# )
# api_router.register(
#     "galleries/<int:pk>/photos/<int:pk>",
#     viewset=views.PhotoViewSet,
#     basename="photo_detail",
# )


# urlpatterns = api_router.urls


urlpatterns = [
    path("galleries/", views.GalleryListCreateView.as_view()),
    path("galleries/<int:gallery_pk>/", views.GalleryRetrieveUpdateDestroy.as_view()),
    # path("photo_list/", views.PhotoList.as_view()),
    # path("photo_detail/", views.PhotoDetail.as_view()),
]
