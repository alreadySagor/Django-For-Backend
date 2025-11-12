from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_genre, name = "add_genre"),
]