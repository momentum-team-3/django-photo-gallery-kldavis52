from django.urls import path
from . import views

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("list_galleries/", views.list_galleries, name="list_galleries"),
    path("create_gallery/", views.create_gallery, name="create_gallery"),
    path(
        "<int:gallery_pk>/gallery_detail/", views.gallery_detail, name="gallery_detail"
    ),
    path("<int:gallery_pk>/add_photo/", views.add_photo, name="add_photo"),
]
