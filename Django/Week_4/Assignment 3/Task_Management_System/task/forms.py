from django import forms
from .models import Task
from django.forms.widgets import NumberInput

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        widgets = {'task_assign_date' : NumberInput(attrs={'type' : 'date'})}