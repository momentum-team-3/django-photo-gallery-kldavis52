# Generated by Django 3.1.1 on 2020-10-01 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photogalle', '0008_auto_20201001_1147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='photo',
            field=models.ManyToManyField(blank=True, related_name='photos', to='photogalle.Photo'),
        ),
    ]