from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('buyer/', include("buyer.urls")),
    path('brand/', include("brand.urls")),
    path('car/', include("car.urls")),
    path('', views.home, name = "homepage"),
]