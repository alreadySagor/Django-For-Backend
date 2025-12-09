from django import forms
from .models import Album
from django.forms.widgets import NumberInput
class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        exclude = ['musician']
        widgets = {'album_release_date' : NumberInput(attrs={'type' : 'date'})}