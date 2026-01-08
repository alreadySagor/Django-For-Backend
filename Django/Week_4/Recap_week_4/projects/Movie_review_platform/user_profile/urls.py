from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_user_profile, name = "add_user_profile"),
]