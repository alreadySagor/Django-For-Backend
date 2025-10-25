from django import forms

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