from django.urls import path
from . import views

urlpatterns = [
    path('add-musician/', views.add_musician, name = "add_musician"),
]