# Generated by Django 4.1 on 2022-08-12 13:19

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0008_likes'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Likes',
            new_name='Like',
        ),
    ]
