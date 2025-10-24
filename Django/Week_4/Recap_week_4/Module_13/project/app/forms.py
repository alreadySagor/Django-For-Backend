from django import forms
from django.core import validators
class contactForm(forms.Form):
    name = forms.CharField(label="Full Name : ", help_text="Total lenth must be within 20 characters", required=False, error_messages={'required': 'Please enter your name.'}, widget= forms.Textarea(attrs = {'id' :'text_area', 'class' : 'class1 class2', 'placeholder' : 'Enter your name'},))
    email = forms.EmailField(label="User Email")

    age = forms.CharField(widget=forms.NumberInput)
    # weight = forms.FloatField()
    # balance = forms.DecimalField()
    check = forms.BooleanField()
    birthday = forms.CharField(widget=forms.DateInput(attrs={'type' : 'date'}))
    appointment = forms.CharField(widget=forms.DateInput(attrs={'type' : 'datetime-local'}))
    CHOISES = [('S', 'Small'), ('M', 'Medium'), ('L', 'Large')]
    size = forms.ChoiceField(choices=CHOISES, widget=forms.RadioSelect)
    meal = [('P', 'Pepperoni'), ('M', 'Mashroom'), ('B', 'Beef')]
    pizza = forms.MultipleChoiceField(choices=meal, widget=forms.CheckboxSelectMultiple)

    # file = forms.FileField()

def len_check(value):
    if len(value) < 10:
        raise forms.ValidationError("Enter a value at least 10 characters")

# class StudentData(forms.Form):
#     name = forms.CharField(widget= forms.TextInput)
#     email = forms.CharField(widget=forms.EmailInput)

#     def clean(self):
#         cleaned_data = super().clean()
#         valname = self.cleaned_data['name']
#         valemail = self.cleaned_data['email']

#         if len(valname) < 10:
#             raise forms.ValidationError("Enter a name with at least 10 characters")
#         if '.com' not in valemail:
#             raise forms.ValidationError("Email must contain .com")


# Django built in Validation
class StudentData(forms.Form):
    name = forms.CharField(widget=forms.TextInput, validators=[validators.MinLengthValidator(10, message="Enter a name with at least 10 characters")])
    email = forms.CharField(widget=forms.EmailInput, validators=[validators.EmailValidator(message="Enter a valid Email")])

    age = forms.IntegerField(validators=[validators.MaxValueValidator(34, message="Age must be maximum 34"), validators.MinValueValidator(24, message="Age must be at least 24")])
    file = forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['pdf', 'png'], message=".pdf .png Only")])
    text = forms.CharField(widget=forms.TextInput, validators=[len_check])


class PasswordValidation(forms.Form):
    name = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
    re_password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        valname = self.cleaned_data['name']
        valpass = self.cleaned_data['password']
        valrepass = self.cleaned_data['re_password']

        if valrepass != valpass:
            raise forms.ValidationError("Password doesn't match")

        if len(valname) < 15:
            raise forms.ValidationError("Name must be at least 10 characters")