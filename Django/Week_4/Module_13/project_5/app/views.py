from django.shortcuts import render
from . forms import contactForm, StudentData, PasswordValidation
# Create your views here.
def about(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        email = request.POST.get('email')
        select = request.POST.get('select')
        return render(request, './app/about.html', {'name' : name, 'email' : email, 'select' : select})
    else:
        return render(request, './app/about.html')

def home(request):
    return render(request, './app/home.html')

def form(request):
    return render(request, './app/form.html')

def django_form(request):
    # form = contactForm()
    # print(form) # shudhu form print korle puro html code show korbe (django form er tuku)
    if request.method == 'POST':
        form = contactForm(request.POST, request.FILES)
        if form.is_valid():
            # file = form.cleaned_data['file']
            # with open('./app/upload/' + file.name, 'wb+') as destination:
            #     for chunk in file.chunks():
            #         destination.write(chunk)
            print(form.cleaned_data) # html code na dekhe shudhu jodi value gula dekhte chai tahole .cleaned_data use korte hobe ar form = contactForm() er () er majhe request.POST use korte hobe and tarpor amake check korte hobe form ta jodi ekta valid form hoy taholei amake output dibe
            # return render(request, 'app/django_form.html', {'form' : form})
    else:
        form = contactForm()
    return render(request, 'app/django_form.html', {'form' : form})

def StudentForm(request):
    if request.method == 'POST':
        form = StudentData(request.POST, request.FILES)
        if form.is_valid():
            print('form.cleaned_data')
    else:
        form = StudentData()
    return render(request, './app/django_form.html', {'form' : form})

def password(request):
    if request.method == 'POST':
        form = PasswordValidation(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = PasswordValidation()
    return render(request, './app/django_form.html', {'form' : form})