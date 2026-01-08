from django.http import HttpResponse

def home(request):
    return HttpResponse("This is Home Page.")

def sagor(request):
    return HttpResponse("This is Sagor.")