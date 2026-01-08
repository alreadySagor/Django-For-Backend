from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about, name = "aboutpage"),
    path('', views.home, name = "app_homepage"),
    path('form/', views.form, name = "formpage"),
    # path('django_form/', views.django_form, name = "django_form"),
    # path('django_form/', views.StudentForm, name = "django_form"),
    path('django_form/', views.password, name = "django_form"),
]