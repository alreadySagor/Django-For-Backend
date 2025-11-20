from django.shortcuts import render, redirect
from . import forms
# Create your views here.
def task(request):
    if request.method == 'POST':
        form = forms.TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("task")
    else:
        form =forms.TaskForm()
    return render(request, 'task.html', {'form' : form})