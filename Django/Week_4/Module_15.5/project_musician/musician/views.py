from django.shortcuts import render, redirect
from .models import Musician
from .forms import MusicianForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def add_musician(request):
    if request.method == 'POST':
        form = MusicianForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("add_musician")
    else:
        form = MusicianForm()
    return render(request, 'add_musician.html', {'form' : form})