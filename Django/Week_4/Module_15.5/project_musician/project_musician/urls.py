from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.view_data, name = "homepage"),
    path('album/', include("album.urls")),
    path('author/', include("author.urls")),
    path('musician/', include("musician.urls")),
]