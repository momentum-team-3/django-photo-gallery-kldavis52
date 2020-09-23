from django.urls import path
from . import views

urlpatterns = [
    path("", views.GalleryList.as_view()),
]
