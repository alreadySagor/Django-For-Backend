from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registration, name = "register"),
    path('login/', views.user_login, name = "login"),
    path('logout/', views.user_logout, name = "logout"),
    path('delete/<int:id>', views.delete_album_musician, name = "delete_album_musician"),
    path('edit/<int:id>', views.edit, name = "edit")
]