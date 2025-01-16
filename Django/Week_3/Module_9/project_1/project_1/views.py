from django.http import HttpResponse

def homepage(request):
    return HttpResponse("This is Home page")
def contact(request):
    return HttpResponse("This is contact page")