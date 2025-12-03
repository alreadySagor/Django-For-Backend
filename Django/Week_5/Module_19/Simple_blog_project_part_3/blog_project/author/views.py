from django.shortcuts import render, redirect
from . import forms
from django.contrib import messages

from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm 
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash

from django.contrib.auth.decorators import login_required
from post.models import Post

from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
#----------------------------------------------------------------------------------------------------------------------
# Create your views here.
# def add_author(request):
#     if request.method == 'POST':
#         author_form = forms.AuthorForm(request.POST)
#         if author_form.is_valid():
#             author_form.save()
#             return redirect("add_author")
#     else:
#         author_form = forms.AuthorForm()
#     return render(request, 'add_author.html', {'form' : author_form})
#----------------------------------------------------------------------------------------------------------------------
def register(request):
    if request.method == 'POST':
        form = forms.RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully')
            return redirect("register")
    else:
        form = forms.RegistrationForm()
    return render(request, 'register.html', {'form' : form, 'type' : 'Register'})
#----------------------------------------------------------------------------------------------------------------------

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            name = form.cleaned_data['username']
            pswd = form.cleaned_data['password']
            user = authenticate(username = name, password = pswd)
            if user is not None:
                login(request, user)
                messages.success(request, 'Logged in successfully')
                return redirect("profile")
            else:
                messages.warning(request, 'Login information Incorrect')
                return redirect("register")
    else:
        form = AuthenticationForm()
        return render(request, 'register.html', {'form' : form, 'type' : 'Login'}) 
        # Register and Login korar jonno ekti matro template use korechi.
        # Ragister korar somoy register korte jesob field lage tar sobkichui register page er jonno kaj korbe.
        # Login korar somoy login korte jesob field lage tar sobkichui login page er jonno kaj korbe
        # 'type' : 'Login' kore deyar fole template er moddhe je {{type}} likhe diyechi sekhane Login lekha dekhabe (Login page e Login ar register page e Register dekhabe)
#--------------------------------------
# Login using class based view
class UserLoginView(LoginView):
    template_name = 'register.html'
    # success_url = reverse_lazy('profile')
    def get_success_url(self):
        return reverse_lazy('profile')
    
    def form_valid(self, form):
        messages.success(self.request, 'Logged in Successful')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.success(self.request, 'Logged in information incorrect')
        return super().form_invalid(form)
    
    # jehetu egister ar login korar jonno ekta template use kortechi tai class based view er moddhe login er jonno Login bole deyar jonno ei fuction ta lekha.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Login'
        return context
#----------------------------------------------------------------------------------------------------------------------
@login_required # ei decorator ta use korar fole (function er upore eitake likhte hoy) kono ekjon use jodi login kora na thake tahole take ei view function ti dekhte dibe na. Redirect kore login page e niye jabe take.
def profile(request):
    # data = Post.objects.all()
    data = Post.objects.filter(author = request.user) # filter kortechi. Jei user request korteche (alada alada user) se shudhu tar post gulai dekhte parbe. (author = request.user) er mane hocche --> oi bekti tai author je ei request korteche. Database theke filter kore antechi.
    return render(request, './profile.html', {'data' : data})

#----------------------------------------------------------------------------------------------------------------------
@login_required # ei decorator ta use korar fole (function er upore eitake likhte hoy) kono ekjon use jodi login kora na thake tahole take ei view function ti dekhte dibe na. Redirect kore login page e niye jabe take.
def edit_profile(request):
    if request.method == 'POST':
        form = forms.ChangeUserData(request.POST, instance = request.user) # request.user --> je user ta request korteche se. Tarmane ei profile e ashte gele age authenticated ba logged in user hote hobe
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
            return redirect("profile")
    else:
        form = forms.ChangeUserData(instance = request.user)
    return render(request, './update_profile.html', {'form' : form})
#----------------------------------------------------------------------------------------------------------------------
@login_required
def pass_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, data = request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Password updated successfully')
            update_session_auth_hash(request, form.user) # eta add korar fole, ami jodi password 123 o dei taholeu kew etake crack korte parbe na, Admin o na.
            return redirect("profile")
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'pass_change.html', {'form' : form})
#----------------------------------------------------------------------------------------------------------------------
def user_logout(request):
    logout(request)
    return redirect("login")
#--------------------------------------
#----------------------------------------------------------------------------------------------------------------------