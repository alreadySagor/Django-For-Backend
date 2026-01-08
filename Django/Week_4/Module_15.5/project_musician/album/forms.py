from django import forms
from .models import Album
from django.forms.widgets import NumberInput
class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'
        # exclude = ['musician']
        widgets = {'album_release_date' : NumberInput(attrs={'type' : 'date'})}