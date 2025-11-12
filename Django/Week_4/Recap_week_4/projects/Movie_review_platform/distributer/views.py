from django.shortcuts import render, redirect
from . import forms
# Create your views here.
def add_distributer(request):
    if request.method == 'POST':
        distributer_form = forms.DistributerForm(request.POST)
        if distributer_form.is_valid():
            distributer_form.save()
            return redirect("add_distributer")
    else:
        distributer_form = forms.DistributerForm()
    return render(request, 'add_distributer.html', {'form' : distributer_form})