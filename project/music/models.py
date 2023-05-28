from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Musics(models.Model):
    """
    Model for storing the audio files
    """
    name = models.CharField(max_length=100)
    music_file = models.FileField(upload_to='media/', verbose_name='file')
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    is_public = models.BooleanField(default=False)

class Permissions(models.Model):
    """
    Model for users having access to music files
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    music = models.ForeignKey(Musics, on_delete=models.CASCADE)

