from django.shortcuts import render, redirect
from . import forms
# Create your views here.
def add_review(request):
    if request.method == 'POST':
        review_form = forms.ReviewForm(request.POST)
        if review_form.is_valid():
            review_form.save()
            return redirect("add_review")
    else:
        review_form = forms.ReviewForm()
    return render(request, 'add_review.html', {'form' : review_form})