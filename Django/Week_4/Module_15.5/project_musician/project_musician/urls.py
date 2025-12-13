from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.view_data, name = "view_data"),
    path('album/', include("album.urls")),
    path('musician/', include("musician.urls")),
]