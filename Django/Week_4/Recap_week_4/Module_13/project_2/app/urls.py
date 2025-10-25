from django.urls import path
from . import views
urlpatterns = [
    path('movies/', views.movies, name = 'movies'),
    path('submit/', views.submitForm, name = 'submit'),
    path('see/', views.seeReview, name = 'see'),
    path('django_form/', views.django_form, name = 'django_form'),
]
