from django.shortcuts import render
from django.http import HttpResponse
import datetime
from . forms import contactForm, StudentData, PasswordValidation
# Create your views here.
def a_home(request):
    return render(request, 'app/a_home.html')

def see_review(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        email = request.POST.get('email')
        rating = request.POST.get('rating')
        review = request.POST.get('review')
        verdict = "0"
        time = datetime.datetime.now()
        if int(request.POST.get('rating')) >= 3:
            verdict = "Good"
        else:
            verdict = "Average"
        return render(request, 'app/see_review.html', {'time': time, 'name' : name, 'email' : email, 'rating' : rating, 'review' : review, 'verdict' : verdict})
    else:
        return render(request, 'app/see_review.html')

def review(request):
    return render(request, 'app/review.html')

def django_form(request):
    if request.method == 'POST':
        form = contactForm(request.POST, request.FILES)
        if form.is_valid():
            # file = form.cleaned_data['file']
            # with open('./app/uploads/' + file.name, 'wb+') as destination:
            #     for chunk in file.chunks():
            #         destination.write(chunk)
            print(form.cleaned_data)
    else:
        form = contactForm()
    return render(request, 'app/django_form.html', {'form' : form})

def StudentForm(request):
    if request.method == 'POST':
        form = StudentData(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = StudentData()
    return render(request, './app/django_form.html', {'form' : form})

def password(request):
    if request.method == 'POST':
        form = PasswordValidation(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = PasswordValidation()
    return render(request, './app/django_form.html', {'form' : form})