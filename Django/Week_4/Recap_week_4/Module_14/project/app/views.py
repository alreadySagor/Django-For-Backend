from django.shortcuts import render, redirect
from . import models, forms
# Create your views here.

def home(request):
    student = models.Student.objects.all()
    return render(request, 'home.html', {'data' : student})

def delete_stdnt(request, roll):
    std = models.Student.objects.get(pk = roll).delete()
    return redirect("homepage")

def add_student(request):
    if request.method == 'POST':
        form = forms.StudentForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = forms.StudentForm()
    return render(request, 'add_student.html', {'form' : form})