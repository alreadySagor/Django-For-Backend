from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def contact(request):
    return HttpResponse("This is Contact Page Under Firstapp.")

def home(request):
    return HttpResponse("This is firstapp/ Home Page.")

def about(request):
    return HttpResponse("This is about page under first app.")