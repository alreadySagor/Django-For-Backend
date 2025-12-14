from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def brand(request):
    return HttpResponse("This is a brand page")