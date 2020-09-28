from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from .models import Gallery, Photo, Comment
from .forms import GalleryForm, PhotoForm, CommentForm

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
    if request.method == "POST":  # user submits form
        form = GalleryForm(request.POST)
        if form.is_valid():
            gallery = form.save(commit=False)
            gallery.user = request.user
            gallery.save()
            return redirect(to="gallery_detail", gallery_pk=gallery.pk)
    form = GalleryForm()
    return render(request, "photogalle/create_gallery.html", {"form": form})


@login_required
def gallery_detail(request, gallery_pk):
    gallery = get_object_or_404(request.user.galleries, pk=gallery_pk)
    photos = Photo.objects.filter(photos=gallery.pk)
    return render(
        request,
        "photogalle/gallery_detail.html",
        {"gallery": gallery, "photos": photos},
    )


@login_required
def add_photo(request, gallery_pk):
    gallery = get_object_or_404(request.user.galleries, pk=gallery_pk)
    if request.method == "POST":  # user submits form
        form = PhotoForm(request.POST, files=request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.user = request.user
            photo.save()
            return redirect(to="gallery_detail", gallery_pk=gallery_pk)
    form = PhotoForm()
    return render(
        request,
        "photogalle/add_photo.html",
        {"form": form, "gallery": gallery},
    )
