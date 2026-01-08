from django.shortcuts import render, redirect
from app.forms import StudentForm
# Create your views here.
def home(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            # form.save(commit = False) # false thakle databse e data save hobe na
            form.save()
            print(form.cleaned_data)
    else:
        form = StudentForm()
    return render(request, './app/home.html', {'form' : form})