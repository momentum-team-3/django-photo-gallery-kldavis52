from django import forms
from .models import Photo, Comment


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = [
            "title",
            "description",
            "photo",
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
