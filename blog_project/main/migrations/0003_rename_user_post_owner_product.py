# Generated by Django 4.1 on 2022-08-05 15:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0002_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='user',
            new_name='owner',
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True, verbose_name='Название')),
                ('desc', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='products/')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='products', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('create_date',),
            },
        ),
    ]