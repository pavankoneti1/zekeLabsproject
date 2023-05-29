from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from pygame import mixer

from .forms import MusicForm
from .models import *
from .serializers import *
# Create your views here.

class MusicViewSet(viewsets.ModelViewSet):
    """
    API end point for uploading the music files
    """
    queryset = Musics.objects.all()
    serializer_class = MusicSerializer
    permission_classes = [IsAuthenticated, ]

    def list(self, request, *args, **kwargs):
        music_form = MusicForm() # form for getting music input
        return render(request, 'music.html', {'form':music_form})

    def create(self, request, *args, **kwargs):
        name = request.POST.get('name')
        music_file = request.POST.get('music_file')
        is_public = request.POST.get('is_public')
        is_protected = request.POST.get('is_protected')
        is_private = request.POST.get('is_private')
        count_value = request.POST.get('submit-btn')
        has_access = [request.POST.get('has_access{}'.format(q)) for q in range(int(count_value))]

        user_id = self.request.user.id
        post_data = request.data
        post_data['uploaded_by'] = user_id
        form = MusicForm(post_data, request.FILES)

        if form.is_valid():
            form.save()
            music_id = self.queryset.latest('id').id

            # login to categorize the audio files public ot private or protected
            if is_public=='on':
                make_public = Musics.objects.get(id=music_id)
                make_public.is_public = True
                make_public.save()

            elif is_protected=='on':
                for mail in has_access:
                    user = User.objects.filter(username=mail).first()
                    if user is not None:
                        user_id = user.id
                        Permissions.objects.create(music_id=music_id, user_id=user_id)
                    else:
                        raise Exception(f"{mail} user dosen't exists")

            else:
                Permissions.objects.create(music_id=music_id, user_id = user_id)

            return Response({"success":True, "message": "Music file successfully uploaded"})

        return Response({"success":False, "message":"data is invalid", "error":form.errors})


class UserMusicViewSet(viewsets.ModelViewSet):
    """
    API end point for display the music files and play
    """
    queryset = Permissions.objects.all()
    serializer_class = MusicSerializer
    permission_classes = [IsAuthenticated, ]

    def list(self, request, *args, **kwargs):
        user_id = self.request.user.id
        public_music_files = Musics.objects.filter(is_public=True).values('music_file')
        music_files = []

        for file in public_music_files:
            music_files.append(file['music_file'])
        music_ids = self.queryset.filter(user_id=user_id).values('music_id')

        for i in music_ids:
            music_files.append(Musics.objects.get(id=i['music_id']).music_file)
        return render(request, 'playMusic.html', {'files':music_files})

    @action(detail=False, methods=['POST'])
    def play(self, request, *args, **kwargs):
        # login to play music files
        file = request.POST.get('file_name')
        mixer.init()
        mixer.music.load(f"E:\PycharmProjects\zekeLabs\project\media\{file}")
        mixer.music.play()

        return Response({"success":True})

