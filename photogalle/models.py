from django.db import models
from users.models import User
from datetime import datetime

# Create your models here.


class Gallery(models.Model):
    private = models.BooleanField(default=False, null=False)
    date_time = models.DateTimeField(auto_now=True, default=datetime.now)
    details = models.ForeignKey(
        to="Details", on_delete=models.CASCADE, null=False, blank=True
    )
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=False, null=False)


class Photo(models.Model):
    photo = True  # django image-kit
    date_time = models.DateTimeField(auto_now=True, default=datetime.now)
    default_image = models.ForeignKey(
        to="Gallery", on_delete=models.CASCADE, blank=True, null=True
    )
    details = models.ForeignKey(
        to="Details", on_delete=models.CASCADE, null=False, blank=True
    )
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=False, null=False)


class Comment(models.Model):
    comment = models.TextField(null=False, blank=True)
    date_time = models.DateTimeField(auto_now=True, default=datetime.now)
    photo = models.ForeignKey(
        to="Photo", on_delete=models.CASCADE, blank=False, null=False
    )
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=False, null=False)


class Details(models.Model):
    title = models.CharField(max_length=511, null=False, blank=True)
    description = models.TextField(null=False, blank=True)
    pinned = models.BooleanField(default=False, null=False)
