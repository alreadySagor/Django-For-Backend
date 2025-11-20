from django.shortcuts import render
from . import forms
# Create your views here.
def djangoForm(request):
    form = forms.ContactForm(request.POST)
    return render(request, 'home.html', {'form' : form})

def modelForm(request):
    form = forms.MForm()
    return render(request, 'home_model.html', {'form' : form})