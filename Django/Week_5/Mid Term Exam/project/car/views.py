from django.shortcuts import render, redirect
from . import forms, models
from django.contrib import messages

from django.contrib.auth.decorators import login_required

# Create your views here.

def add_car(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = forms.CarForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Car added successfully')
                return redirect("homepage")
        else:
            form = forms.CarForm()
        return render(request, 'add_car.html', {'form' : form})
    else:
        return redirect("register")

def car_details(request, id):
    car = models.Car.objects.get(pk = id)
    if request.method == 'POST':
        form = forms.CommentForm(request.POST)
        if form.is_valid():
            new_form =  form.save(commit=False)
            new_form.car = car
            new_form.save()
            messages.success(request, 'Comment added successfully')
            return redirect("homepage")
    else:
        form = forms.CommentForm()
    comment = car.comment.all()
    return render(request, 'car_details.html', {'form' : form, 'car' : car, 'comment' : comment})