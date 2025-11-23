from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Account created successfully')
            messages.info(request, 'Welcome')
            messages.warning(request, 'This is a warning message')
            form.save()
            return redirect("signup")
    else:
        form = RegisterForm()
    return render(request, 'signup.html', {'form' : form})