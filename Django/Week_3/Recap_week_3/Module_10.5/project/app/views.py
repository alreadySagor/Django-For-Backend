from django.shortcuts import render

# Create your views here.
def app(request):
    return render(request, 'app/app.html')

def about(request):
    return render(request, 'app/about.html')

def contact(request):
    return render(request, 'app/contact.html')