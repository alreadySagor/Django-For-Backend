from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.view_data, name = "view_data"),
    path('album/', include("album.urls")),
    path('musician/', include("musician.urls")),
    path('delete/<int:id>', views.delete_album_musician, name = "delete_album_musician"),
    path('edit/<int:id>', views.edit, name = "edit")
]