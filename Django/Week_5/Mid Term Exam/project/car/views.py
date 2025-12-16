from django.shortcuts import render, redirect
from . import forms, models
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView

# Create your views here.
#----------------------------------------------------------------------------------------------------------------------
class AddCarCreateView(CreateView):
    model = models.Car
    form_class = forms.CarForm
    template_name = "add_car.html"
    success_url = reverse_lazy('homepage')
    
#----------------------------------------------------------------------------------------------------------------------
class DetailsCarView(DetailView):
    model = models.Car
    template_name = "car_details.html"
    pk_url_kwarg = 'id'

    def car(self, request, *args, **kwargs):
        form = forms.CommentForm(data=self.request.POST)
        car = self.get_object()
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.car = car
            new_form.save()
        return self.get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        car = self.object()
        comment = car.comment.all()
        form = forms.CommentForm()

        context['comment'] = comment
        context['form'] = form
        return context
#----------------------------------------------------------------------------------------------------------------------

# def add_car(request):
#     if request.user.is_authenticated:
#         if request.method == 'POST':
#             form = forms.CarForm(request.POST)
#             if form.is_valid():
#                 form.save()
#                 messages.success(request, 'Car added successfully')
#                 return redirect("homepage")
#         else:
#             form = forms.CarForm()
#         return render(request, 'add_car.html', {'form' : form})
#     else:
#         return redirect("register")

# def car_details(request, id):
#     car = models.Car.objects.get(pk = id)
#     if request.method == 'POST':
#         form = forms.CommentForm(request.POST)
#         if form.is_valid():
#             new_form =  form.save(commit=False)
#             new_form.car = car
#             new_form.save()
#             messages.success(request, 'Comment added successfully')
#             return redirect("homepage")
#     else:
#         form = forms.CommentForm()
#     comment = car.comment.all()
#     return render(request, 'car_details.html', {'form' : form, 'car' : car, 'comment' : comment})