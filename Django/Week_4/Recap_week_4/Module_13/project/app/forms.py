from django import forms

class contactForm(forms.Form):
    name = forms.CharField(label="User Name")
    emai = forms.EmailField(label="User Email")