# Generated by Django 3.1.1 on 2020-09-25 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photogalle', '0006_auto_20200925_1815'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='gallery',
        ),
        migrations.AddField(
            model_name='gallery',
            name='photo',
            field=models.ManyToManyField(blank=True, related_name='photos', to='photogalle.Photo'),
        ),
    ]