from django import forms
from .models import Musics, Permissions

class MusicForm(forms.ModelForm):
    class Meta:
        model = Musics
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(MusicForm, self).__init__(*args, **kwargs)
        self.fields['uploaded_by'].required = False
