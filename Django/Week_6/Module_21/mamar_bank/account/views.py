from django.shortcuts import render, redirect
from django.views.generic import FormView
from . forms import UserRagistrationForm
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
# Create your views here.
class UserRegistrationView(FormView):
    template_name = "account/registration.html"
    form_class = UserRagistrationForm
    success_url = reverse_lazy("register")

    def form_valid(self, form):
        print(form.cleaned_data)
        # user = form.save() # je 3 ta model create korechi sei 3 ta model e data save hoye jabe. (save function call korechi ar return value hisebe our_user er pacchi)
        # login(user) # user er data gula diye login kore dilam. (registation form theke prapto data gula diye sorasori login kore dilam)
        return super().form_valid(form) # form_valid function ta call hobe jodi sob thik thake
    