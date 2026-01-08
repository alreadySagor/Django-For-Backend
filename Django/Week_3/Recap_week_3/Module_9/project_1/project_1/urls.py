from django.contrib import admin
from django.urls import path, include
# from .views import contact
from . import views  # same as "from .views import contact" shudhu path er moddhe contact er age views. ta add korte hobe

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('first_app/', include("first_app.urls")),
    path('contact/', views.contact),
]
