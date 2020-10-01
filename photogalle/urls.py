from django.urls import path
from . import views

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("list_galleries/", views.list_galleries, name="list_galleries"),
    path("list_galleries/create_gallery/", views.create_gallery, name="create_gallery"),
    path(
        "list_galleries/<int:gallery_pk>/", views.gallery_detail, name="gallery_detail"
    ),
    path(
        "list_galleries/<int:gallery_pk>/add_photo/", views.add_photo, name="add_photo"
    ),
]
