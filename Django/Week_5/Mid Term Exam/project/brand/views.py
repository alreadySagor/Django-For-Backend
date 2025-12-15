from django.shortcuts import render, redirect
from .forms import BrandForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

def add_brand(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = BrandForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Brand added Successfully')
                return redirect("add_brand")
        else:
            form = BrandForm()
        return render(request, 'add_brand.html', {'form' : form})
    else:
        return redirect("register")
