from django import forms
from django.core import validators

# widgets == field to html input
class contactForm(forms.Form):
    name = forms.CharField(label="Full Name : ", help_text="Total length must be within 70 characters", required=False, widget=forms.Textarea(attrs = {'id' : 'text_area', 'class' : 'class1 class2', 'placeholder' : 'Enter your Name'})) #disabled=True)
    email = forms.EmailField(label="User Email")

    file = forms.FileField() # to upload files. 

    # age = forms.IntegerField()
    # weight = forms.FloatField()
    # balance = forms.DecimalField()
    age = forms.CharField(widget=forms.NumberInput) # jodi field er naam mone na thake je float nibo naki decimal nibo? tokhon eta use korte pari
    check = forms.BooleanField()
    birthday = forms.CharField(widget=forms.DateInput(attrs = {'type' : 'date'}))
    appointment = forms.CharField(widget=forms.DateInput(attrs = {'type' : 'datetime-local'}))

    CHOICES = [('S', 'Small'), ('M', 'Medium'), ('L', 'Large')]
    size = forms.ChoiceField(choices=CHOICES, widget = forms.RadioSelect)

    Meal = [('P', "Pepperoni"), ('M', 'Mashroom'), ('B', 'Beef')]
    pizza = forms.MultipleChoiceField(choices=Meal, widget = forms.CheckboxSelectMultiple)


# class StudentData(forms.Form):
#     name = forms.CharField(widget = forms.TextInput)
#     email = forms.CharField(widget = forms.EmailInput)
#     # def clean_name(self):
#     #     valname = self.cleaned_data['name']
#     #     if len(valname) < 10:
#     #         raise forms.ValidationError("Enter a name with at leat 10 characters")
#     #     return valname
    
#     # def clean_email(self):
#     #     valemail = self.cleaned_data['email']
#     #     if '.com' not in valemail:
#     #         raise forms.ValidationError("Your Email must contain .com")
#     #     return valemail

#     # validation gula alada alada function e na likhe ekta function e likhe felbo
#     def clean(self):
#         cleaned_data = super().clean()
#         valname = self.cleaned_data['name']
#         valemail = self.cleaned_data['email']
#         if len(valname) < 10:
#             raise forms.ValidationError("Enter a name with at leat 10 characters")
#         if '.com' not in valemail:
#             raise forms.ValidationError("Your Email must contain .com")


def len_check(value):
    if len(value) < 10:
        raise forms.ValidationError("Enter a value at least 10 characters")
# Built in Form Validators
class StudentData(forms.Form):
    # amra je custom function gula toiri kortechi oigula validators er moddhe use korte parbo
    text = forms.CharField(widget=forms.TextInput, validators=[len_check])

    name = forms.CharField(widget = forms.TextInput, validators = [validators.MinLengthValidator(10, message="Enter a name with at least 10 characters")])
    email = forms.CharField(widget = forms.EmailInput, validators = [validators.EmailValidator(message="Enter Valid Email")])
    age = forms.IntegerField(validators=[validators.MaxValueValidator(34, message="Age must be maximum 34"), validators.MinValueValidator(24, message="age must be at leat 24")])

    file = forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['pdf'], message="File Extension must be ended with .pdf")])

class PasswordValidation(forms.Form):
    name = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        val_pass = self.cleaned_data['password']
        re_val_pass = self.cleaned_data['confirm_password']
        val_name = self.cleaned_data['name']
        if re_val_pass != val_pass:
            raise forms.ValidationError("Password doesn't match")
        
        if len(val_name) < 15:
            raise forms.ValidationError("Name must be at least 15 characters")