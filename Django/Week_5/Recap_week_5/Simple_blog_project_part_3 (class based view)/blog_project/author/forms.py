from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# class AuthorForm(forms.ModelForm):
#     class Meta:
#         model = Author
#         fields = '__all__' # sobkichu niyei ekta form toiri hoye jabe
        # fields = ['name', 'bio'] # name ar bio niye ekta form toiri hoye jabe
        # exclude = ['bio'] # bio ta bad diye baki ja kichu ache segula niye ekta form toiri hoye jabe.

class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'id' : 'required'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'id' : 'required'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'id' : 'required'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class ChangeUserData(UserChangeForm):
    password = None
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']