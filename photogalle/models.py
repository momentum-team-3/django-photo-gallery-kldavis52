from django.db import models
from users.models import User
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit, ResizeToFill

# Create your models here.


class Gallery(models.Model):
    private = models.BooleanField(default=False, null=False)
    date_time = models.DateTimeField(auto_now=True)
    detail = models.ForeignKey(
        to="Detail",
        on_delete=models.CASCADE,
        null=False,
        blank=True,
        related_name="galleries",
    )
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        related_name="galleries",
    )


class Photo(models.Model):
    photo = models.ImageField(upload_to="photogalle/", null=True, blank=True)
    photo_medium = ImageSpecField(
        source="image",
        processors=[ResizeToFit(300, 300)],
        format="JPEG",
        options={"quality": 80},
    )
    photo_thumbnail = ImageSpecField(
        source="image",
        processors=[ResizeToFill(150, 150)],
        format="JPEG",
        options={"quality": 80},
    )
    date_time = models.DateTimeField(auto_now=True)
    pinned = models.BooleanField(default=False, null=False)
    gallery = models.ForeignKey(
        to="Gallery",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="photos",
    )
    detail = models.ForeignKey(
        to="Detail",
        on_delete=models.CASCADE,
        null=False,
        blank=True,
        related_name="photos",
    )
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        related_name="photos",
    )


class Comment(models.Model):
    comment = models.TextField(null=False, blank=True)
    date_time = models.DateTimeField(auto_now=True)
    photo = models.ForeignKey(
        to="Photo",
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        related_name="comments",
    )
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        related_name="comments",
    )


class Detail(models.Model):
    title = models.CharField(max_length=511, null=False, blank=True)
    description = models.TextField(null=False, blank=True)
