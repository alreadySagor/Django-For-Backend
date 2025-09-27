from django.urls import path
# from .views import contact
from . import views  # same as "from .views import contact" shudhu path er moddhe contact er age views. ta add korte hobe

urlpatterns = [
    path('courses/', views.courses),
    path('about/', views.about),
    path('', views.home),
]