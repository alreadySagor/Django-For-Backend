from django.urls import path
from . import views
urlpatterns = [
    path('signup/', views.signup, name = "signup"),
    path('login/', views.user_login, name = "login"),
    path('logout/', views.user_logout, name = "logout"),
    path('change-password/', views.pass_change, name = "passchange"),
    path('change-password_2/', views.pass_change_2, name = "passchange_2"),
    path('', views.home, name = "homepage"),
    path('profile/', views.profile, name = "profile"),
]