from django.urls import path
from . import views

urlpatterns = [
    path('add-task/', views.task, name = "task"),
]
