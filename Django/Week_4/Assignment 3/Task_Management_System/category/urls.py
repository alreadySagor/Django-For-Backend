from django.urls import path
from . import views

urlpatterns = [
    path('add-category/', views.category, name = "category"),
]