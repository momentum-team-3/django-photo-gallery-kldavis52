# Generated by Django 3.1.1 on 2020-09-17 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photogalle', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gallery',
            old_name='details',
            new_name='detail',
        ),
        migrations.RenameField(
            model_name='photo',
            old_name='details',
            new_name='detail',
        ),
        migrations.RemoveField(
            model_name='detail',
            name='pinned',
        ),
        migrations.AddField(
            model_name='photo',
            name='pinned',
            field=models.BooleanField(default=False),
        ),
    ]
