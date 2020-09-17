from django import forms
from .models import Gallery, Photo, Comment, Detail


class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = [
            "private",
        ]

        widgets = {
            "private": forms.BooleanField(required=False),
        }


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = [
            "photo",
            "pinned",
        ]
        widgets = {
            "pinned": forms.BooleanField(required=False),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            "comment",
        ]
        widgets = {"comment": forms.Textarea()}


class DetailForm(forms.ModelForm):
    class Meta:
        model = Detail
        fields = [
            "title",
            "description",
        ]
        widgets = {
            "title": forms.TextInput(),
            "description": forms.Textarea(),
        }
