# Generated by Django 4.2.1 on 2023-05-26 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_permissions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musics',
            name='music_file',
            field=models.FileField(upload_to='media/'),
        ),
    ]
