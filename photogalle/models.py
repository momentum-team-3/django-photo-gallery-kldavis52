from django.db import models
from users.models import User
from datetime import datetime
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit, ResizeToFill

# Create your models here.


class Gallery(models.Model):
    private = models.BooleanField(default=False, null=False)
    date_time = models.DateTimeField(auto_now=True)
    details = models.ForeignKey(
        to="Details", on_delete=models.CASCADE, null=False, blank=True
    )
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=False, null=False)


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
        processors=[ResizeToFill(300, 300)],
        format="JPEG",
        options={"quality": 80},
    )
    date_time = models.DateTimeField(auto_now=True)
    default_image = models.ForeignKey(
        to="Gallery", on_delete=models.CASCADE, blank=True, null=True
    )
    details = models.ForeignKey(
        to="Details", on_delete=models.CASCADE, null=False, blank=True
    )
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=False, null=False)

    def aws_directory_path(self):
        # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
        return "user_{0}/{1}".format(self.user.id, self.details.title)


class Comment(models.Model):
    comment = models.TextField(null=False, blank=True)
    date_time = models.DateTimeField(auto_now=True)
    photo = models.ForeignKey(
        to="Photo", on_delete=models.CASCADE, blank=False, null=False
    )
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=False, null=False)


class Details(models.Model):
    title = models.CharField(max_length=511, null=False, blank=True)
    description = models.TextField(null=False, blank=True)
    pinned = models.BooleanField(default=False, null=False)
