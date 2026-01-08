from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def courses(request):
    return HttpResponse("This is first app / Courses page.")

def about(request):
    return HttpResponse("This is first app / About Page.")

def first_app(request):
    return HttpResponse("This is first app page.")