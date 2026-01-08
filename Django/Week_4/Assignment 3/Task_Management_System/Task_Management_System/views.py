from django.shortcuts import render, redirect
from task.models import Task
from task import forms

def view_task(request):
    data = Task.objects.all()
    return render(request, 'view_task.html', {'data' : data})

def delete_task(request, id):
    task = Task.objects.get(pk = id)
    task.delete()
    return redirect("view_task")

def edit_task(request, id):
    task = Task.objects.get(pk = id)
    task_form = forms.TaskForm(instance = task)
    if request.method == 'POST':
        task_form = forms.TaskForm(request.POST, instance = task)
        if task_form.is_valid():
            task_form.save()
            return redirect("view_task")
    return render(request, 'task.html', {'form' : task_form})