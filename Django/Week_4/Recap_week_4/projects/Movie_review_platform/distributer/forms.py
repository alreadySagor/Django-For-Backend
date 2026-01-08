from django import forms
from . models import Distributer

class DistributerForm(forms.ModelForm):
    class Meta:
        model = Distributer
        fields = '__all__'