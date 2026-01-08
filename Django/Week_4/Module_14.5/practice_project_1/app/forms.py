from django import forms
from django.forms.widgets import NumberInput
from .models import StudentModel

class ContactForm(forms.Form):
    name = forms.CharField(max_length=50, label="Enter your name")
    email = forms.EmailField(label="Please enter your email address")
    about = forms.CharField(widget=forms.Textarea(attrs={'rows' : 3}))
    url = forms.URLField(initial="https://")
    birthday = forms.DateField(widget=NumberInput(attrs={'type' : 'date'}))
    FAV_COLORS = [('blue', 'Blue'), ('green', 'Green'), ('black', 'Black'),]
    favorite_color = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=FAV_COLORS)
    agree = forms.BooleanField()


class MForm(forms.ModelForm):
    class Meta:
        model = StudentModel
        fields = '__all__'