from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Gallery, Photo, Comment, Detail
from .forms import GalleryForm, PhotoForm, CommentForm, DetailForm

# Create your views here.


def homepage(request):
    return render(request, "photogalle/homepage.html")


@login_required
def list_galleries(request):
    if not request.user.is_authenticated:
        return redirect(to="auth_login")
    galleries = Gallery.objects.filter(private=False)
    return render(request, "photogalle/list_galleries.html", {"galleries": galleries})


@login_required
def create_gallery(request):
    pass
