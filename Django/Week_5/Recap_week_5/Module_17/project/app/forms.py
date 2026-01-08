from django.contrib.auth.models import User # built-in user model, tai notun kore ar model ba form create korte hoyna. Just User ke inherite korbo

# form toiri korar jonno ( "UserCreationForm" eta built in tai shudhu etake inherite korlei hobe)
# user er data edit/update/change korte chaile "UserChangeForm" Use korte pari
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
class RegisterForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'id' : 'required'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'id' : 'required'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'id' : 'required'}))
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
        ]
# Ekhane password field ta dei nai. Kintu tarporo django automatically password
# field take niye nibe. Er karon ekta user create korte chaile password ditei hobe ba thaktei hobe

class ChangeUserData(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
        ]