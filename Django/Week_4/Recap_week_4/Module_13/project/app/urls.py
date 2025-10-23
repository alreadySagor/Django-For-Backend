from django.urls import path
from . import views

urlpatterns = [
    path('', views.a_home), #name="app"
    path('see_review/', views.see_review), #, name="movie"
    path('review/', views.review), #, name="review"
    path('django_form/', views.django_form),
]