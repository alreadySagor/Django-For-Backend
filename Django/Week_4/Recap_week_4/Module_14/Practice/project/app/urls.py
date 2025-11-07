from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "homepage"),
    path('delete/<int:roll>', views.delete_stdnt, name = "delete_stdnt"),
    path('add/', views.add_student, name = "add_student")
]