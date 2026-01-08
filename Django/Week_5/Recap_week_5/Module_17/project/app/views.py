from django.shortcuts import render, redirect
from .forms import RegisterForm, ChangeUserData
from django.contrib import messages # kono kaj sompurno korar por message show korate chaile eta import korte pari, eta built-in ekta jinis tai project er sobkhanei etake access korte parbo

# ei built-in "Authentication" form tate username ar password field ta thake sadharonoto" --> Login korar jonno username, ar pass diye database e check korar jonno
# "PasswordChangeForm" old password diye password change korte use kora hoy
# "SetPasswordForm" old password charai password change korte use kora
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm

# login logout korar jonno (django bultin vabei dicche amaderke)
# "update_session_auth_hash" user er jei password thakbe seta jodi hash/hassing hoye jay, orthat jinish ta jodi besh kichu complex jinish amader samne show kore oi jinish ta jate update hoye jay tai amra ei function take call korbo 
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash

def home(request):
    return render(request, 'home.html')


def signup(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                messages.success(request, 'Account created successfully')
                messages.warning(request, 'warning')
                messages.info(request, 'info')
                form.save() # Bracket er vitore "commit = False" dile data gula databse e save hobe na. Save korar jonno "commit = True" othoba faka rakhte pari
                # print(form.cleaned_data)
                return redirect("signup")
        else:
            form = RegisterForm()
        return render(request, 'signup.html', {'form' : form})
    else:
        return redirect("profile")
    

def user_login(request):
    if not request.user.is_authenticated: # jodi authenticate user ba login kora nei emon user thakle aage login korte hobe. (signup er khetrew same, signup ba register kora thaklei to login kora possible)
        if request.method == 'POST':
            form = AuthenticationForm(request = request, data = request.POST) # reqeust ta access kortechi ar user je data gula dibe segula access kortechi
            if form.is_valid():
                name = form.cleaned_data['username']
                pswd = form.cleaned_data['password']
                user = authenticate(username = name, password = pswd) # check kortechi user database e ache kina (user ekti object)
                if user is not None: # user ke databse e na pele None pabo, Ar None na pele login korte parbe
                    login(request, user) # request take ar user ke pass kore dicchi, tarpor login hoye jabe
                    return redirect("profile")
        else:
            form = AuthenticationForm()
        return render(request, 'login.html', {'form' : form})
    else: # jodi authenticate ba login kora ache emon user thakle se ar signup, login page access korte parbe na. signup, login page access korte chaile redirect kore profile page e niye jawa hobe
        return redirect("profile")
    

def profile(request):
    # return render(request, 'profile.html', {'user' : request.user})
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ChangeUserData(request.POST, instance = request.user) # request.user --> jei user ti login kora ache seta
            if form.is_valid():
                messages.success(request, 'Account updated successfully')
                form.save() # Bracket er vitore "commit = False" dile data gula databse e save hobe na. Save korar jonno "commit = True" othoba faka rakhte pari
                # print(form.cleaned_data)
        else:
            form = ChangeUserData(instance = request.user) # "instance = request.user" dile user er previous data gula form er moddhe show korbe
        return render(request, 'profile.html', {'form' : form})
    else:
        return redirect("signup")
    
def user_logout(request):
    logout(request) # user request korteche logout korar jonno, and logout hoye jabe.
    return redirect("login")

def pass_change(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(user = request.user, data = request.POST) # PasswordChangeForm ta user pass korbe jekina ekjon authenticate user. user ke pass korbo je user ti authenticate, karon authenticate user chara to password kew change korte parbena.
            if form.is_valid():
                form.save()
                # password update korbe
                update_session_auth_hash(request, form.user) # ekta request parameter accept kore, & amra form.user ke pass kore dibo.... User je password ti change korteche seta etar (update_session_auth_hash) maddhome change hoye jabe
                return redirect("profile")
        else:
            form = PasswordChangeForm(user = request.user) # user er old password ta jodi show korate chai tahole () er vitore "user = request.user" dite hobe. Bracket er vitore kichu na dilew kono somossha nai (na dile old password ta show korano jabe na).
        return render(request, 'pass_change.html', {'form' : form})
    else:
        return redirect("login")

def pass_change2(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = SetPasswordForm(user = request.user, data = request.POST) # PasswordChangeForm ta user pass korbe jekina ekjon authenticate user. user ke pass korbo je user ti authenticate, karon authenticate user chara to password kew change korte parbena.
            if form.is_valid():
                form.save()
                # password update korbe
                update_session_auth_hash(request, form.user) # ekta request parameter accept kore, & amra form.user ke pass kore dibo.... User je password ti change korteche seta etar (update_session_auth_hash) maddhome change hoye jabe
                return redirect("profile")
        else:
            form = SetPasswordForm(user = request.user) # user er old password ta jodi show korate chai tahole () er vitore "user = request.user" dite hobe. Bracket er vitore kichu na dilew kono somossha nai (na dile old password ta show korano jabe na).
        return render(request, 'pass_change.html', {'form' : form})
    else:
        return redirect("login")    