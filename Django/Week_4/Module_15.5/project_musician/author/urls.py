from django.urls import path
from . import views

urlpatterns = [
    path('add-musician/', views.add_musician, name = "add_musician"),
    path('delete/<int:id>', views.delete_album_musician, name = "delete_album_musician"),
    path('edit/<int:id>', views.edit, name = "edit")
]