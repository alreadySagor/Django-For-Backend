from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse("This is first app/Home Page.")
def courses(request):
    return HttpResponse("This is first app/courses Page.")
def about(request):
    return HttpResponse("This is first app/About Page.")