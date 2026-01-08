from django import forms
from django.core import validators

class djangoForm(forms.Form):
    name = forms.CharField(label="Full Name : ", help_text="Toal length must be within 20 characters", required=False, error_messages={'required' : "Please enter your name."}, widget=forms.Textarea(attrs={'id' : 'text_area', 'class' : 'class1 class2', 'placeholder' : 'Enter your name'},))
    email = forms.EmailField(label="User Email")

    birthday = forms.CharField(widget=forms.DateInput(attrs={'type' : 'date'}))
    appointment = forms.CharField(widget=forms.DateInput(attrs={'type' : 'datetime-local'}))
    CHOICES = [('S', 'Small'), ('M', 'Medium'), ('L', 'Large')]
    size = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    MEAL = [('C', 'Chicken'), ('M', 'Mutton'), ('B', 'Beef')]
    dish = forms.MultipleChoiceField(choices=MEAL, widget=forms.CheckboxSelectMultiple)

    # file = forms.FileField()

def len_check(value):
    if len(value) < 10:
        raise forms.ValidationError("Enter a value at least 10 characters.")

class StudentData(forms.Form):
    # name = forms.CharField(widget=forms.TextInput)
    # email = forms.CharField(widget=forms.EmailInput)

    # def clean(self):
    #     cleaned_data = super().clean()
    #     val_name = self.cleaned_data['name']
    #     val_email = self.cleaned_data['email']
    #     if len(val_name) < 10:
    #         raise forms.ValidationError("Enter a name with at least 10 characters.")
    #     if '.com'not in val_email:
    #         raise forms.ValidationError("Email must contain .com")

    name = forms.CharField(validators=[validators.MinLengthValidator(10, message="Enter a name with at least 10 characters")])

    email = forms.CharField(validators=[validators.EmailValidator(message="Enter a valid Email")])

    age = forms.IntegerField(validators=[validators.MaxValueValidator(34, message="age must be maximum 34"), validators.MinValueValidator(24, message="age must be at least 24")])

    # file = forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['jpeg'], message=".jpeg only")])

    text = forms.CharField(widget=forms.TextInput, validators=[len_check])


class PasswordCheck(forms.Form):
    name = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
    re_password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        val_name = self.cleaned_data['name']
        val_password = self.cleaned_data['password']
        val_re_password = self.cleaned_data['re_password']

        if len(val_name) < 10:
            raise forms.ValidationError("Name must be at least 10 characters")
        if val_password != val_re_password:
            raise forms.ValidationError("Password doesn't match")