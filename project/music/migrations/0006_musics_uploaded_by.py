# Generated by Django 4.2.1 on 2023-05-27 19:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('music', '0005_remove_permissions_is_private_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='musics',
            name='uploaded_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]