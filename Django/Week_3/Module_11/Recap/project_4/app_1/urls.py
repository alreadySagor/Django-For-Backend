from django.urls import path
from . import views
urlpatterns = [
    # name = 'Home' means this is home url
    path('', views.index, name = 'home'),
    path('about/', views.about, name = 'about'),
]