from django import forms
from .models import Gallery, Photo, Comment


class GalleryForm(forms.ModelForm):
    private = forms.BooleanField(widget=forms.CheckboxInput, required=False)

    class Meta:
        model = Gallery
        fields = [
            "title",
            "description",
            "private",
        ]

        widgets = {
            "title": forms.TextInput(),
            "description": forms.Textarea(),
        }


class PhotoForm(forms.ModelForm):
    pinned = forms.BooleanField(widget=forms.CheckboxInput, required=False)

    class Meta:
        model = Photo
        fields = [
            "title",
            "description",
            "image",
            "pinned",
        ]
        widgets = {
            "title": forms.TextInput(),
            "description": forms.Textarea(),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            "comment",
        ]
        widgets = {"comment": forms.Textarea()}
