from django.shortcuts import render
from . form import djangoForm, StudentData, PasswordCheck
import datetime
# Create your views here.
def movies(request):
    return render(request, './app/movies.html')

def submitForm(request):
    return render(request, './app/submit.html')

def seeReview(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        email = request.POST.get('email')
        review = request.POST.get('review')
        rating = request.POST.get('select')
        time = datetime.datetime.now()

        verdict = ""
        if int(request.POST.get('select')) >= 3 and int(request.POST.get('select')) <= 5:
            verdict = "Good"
        elif int(request.POST.get('select')) >= 1 and int(request.POST.get('select')) < 2:
            verdict = "Poor"
        else:
            verdict = "Average"
        return render(request, './app/see.html', {'name' : name, 'email' : email, 'review' : review, 'rating' : rating, 'time' : time, 'verdict' :verdict})
    else:    
        return render(request, './app/see.html')
    

def django_form(request):
    if request.method == 'POST':
        form = djangoForm(request.POST, request.FILES)
        if form.is_valid():
            # file = form.cleaned_data['file']
            # with open('./app/uploads/' + file.name, 'wb+') as destination:
            #     for chunk in file.chunks():
            #         destination.write(chunk)
            print(form.cleaned_data)
    else:
        form = djangoForm()
    return render(request, './app/django_form.html', {'form' : form})

def student(request):
    if request.method == 'POST':
        form = StudentData(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = StudentData()
    return render(request, './app/django_form.html', {'form' : form})

def password_matcing(request):
    if request.method == 'POST':
        form = PasswordCheck(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = PasswordCheck()
    return render(request, './app/django_form.html', {'form' : form})