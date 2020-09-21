# Generated by Django 3.1.1 on 2020-09-18 01:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('photogalle', '0003_auto_20200917_2006'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photo',
            old_name='photo',
            new_name='image',
        ),
        migrations.RemoveField(
            model_name='gallery',
            name='detail',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='detail',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='gallery',
        ),
        migrations.AddField(
            model_name='gallery',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='gallery',
            name='photo',
            field=models.ManyToManyField(blank=True, related_name='photos', to='photogalle.Photo'),
        ),
        migrations.AddField(
            model_name='gallery',
            name='title',
            field=models.CharField(blank=True, max_length=511),
        ),
        migrations.AddField(
            model_name='photo',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='photo',
            name='title',
            field=models.CharField(blank=True, max_length=511),
        ),
        migrations.AlterField(
            model_name='comment',
            name='photo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photogalle.photo'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='photo',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Detail',
        ),
    ]