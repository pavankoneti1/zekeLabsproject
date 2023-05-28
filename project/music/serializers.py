from rest_framework.serializers import ModelSerializer
from .models import Musics

class MusicSerializer(ModelSerializer):
    class Meta:
        model = Musics
        fields = "__all__"
