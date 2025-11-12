from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_distributer, name = "add_distributer"),
]