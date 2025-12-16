from django.shortcuts import render, redirect
from .forms import RegistrationForm, ChangeUserData
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from car.models import Car
from car.forms import CarForm
from .forms import BuyForm
from django.db import transaction
from .models import Buy
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import UpdateView

# Create your views here.
#----------------------------------------------------------------------------------------------------------------------
class BuyerLoginView(LoginView):
    template_name = "regi_login.html"
    def get_success_url(self):
        return reverse_lazy('profile')
    def form_valid(self, form):
        messages.success(self.request, 'Logged in Successful')
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.success(self.request, 'Login Information Incorrect')
        return super().form_invalid(form)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Login'
        return context
#----------------------------------------------------------------------------------------------------------------------
class EditBuyerView(UpdateView):
    model = User
    form_class = ChangeUserData
    template_name = "update_profile.html"
    success_url = reverse_lazy("profile")

    def get_object(self):
        return self.request.user
    
    def form_valid(self, form):
        messages.success(self.request, 'Profile Updated Successfully')
        return super().form_valid(form)
    
#----------------------------------------------------------------------------------------------------------------------


def registration(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = RegistrationForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Account Created Successfully')
                return redirect("login")
        else:
            form = RegistrationForm()
        return render(request, 'regi_login.html', {'form' : form, 'type' : 'Registration'})
    else:
        return redirect("profile")

# def user_login(request):
#     if not request.user.is_authenticated:
#         if request.method == 'POST':
#             form = AuthenticationForm(request, request.POST)
#             if form.is_valid():
#                 name = form.cleaned_data['username']
#                 pswd = form.cleaned_data['password']
#                 user = authenticate(username = name, password = pswd)
#                 if user is not None:
#                     login(request, user)
#                     messages.success(request, 'Logged in Successful')
#                     return redirect("profile")
#         else:
#             form = AuthenticationForm(request)
#         return render(request, 'regi_login.html', {'form' : form, 'type' : 'Login'})
#     else:
#         return redirect("profile")

def user_logout(request):
    logout(request)
    return redirect("login")


def profile(request):
    if request.user.is_authenticated:
        form = User.objects.filter(id = request.user.id)
        data = Buy.objects.filter(user = request.user)
        return render(request, 'profile.html', {'form' : form, 'data' : data})
    else:
        return redirect("register")

# def edit_profile(request):
#     if request.user.is_authenticated:
#         if request.method == 'POST':
#             form = ChangeUserData(request.POST, instance = request.user)
#             if form.is_valid():
#                 form.save()
#                 messages.success(request, 'Profile Updated Successfully')
#                 return redirect("profile")
#         else:
#             form = ChangeUserData(instance = request.user)
#         return render(request, 'update_profile.html', {'form' : form})
#     else:
#         return redirect("register")

def pass_change(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(request.user, request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Password Updated Successfully')
                update_session_auth_hash(request, form.user)
                return redirect("profile")
        else:
            form = PasswordChangeForm(request.user)
        return render(request, 'pass_change.html', {'form' : form})
    else:
        return redirect("register")


def buy_car(request, id):
    car = get_object_or_404(Car, pk=id)
    if car.quantity < 1:
        messages.error(request, 'Sorry! This car is out of stock.')
        return redirect("profile")
    
    if request.method == 'POST':
        with transaction.atomic():
            Buy.objects.create(
                user = request.user,
                car = car,
                brand = car.brand,
                model_name = car.model_name,
                price = car.price,
                image = car.image,
                features = car.features,
            )
            car.quantity -= 1
            car.save()
        messages.success(request, 'Congratulations! Successfully bought this car.')
        return redirect("profile")
    return redirect("profile")