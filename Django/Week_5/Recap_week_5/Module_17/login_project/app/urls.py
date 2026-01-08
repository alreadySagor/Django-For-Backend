from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name = "homepage"),
    path('signup/', views.user_signup, name = "signup"),
    path('login/', views.user_login, name = "login"),
    path('logout/', views.user_logout, name = "logout"),
    path('profile/', views.profile, name = "profile"),
    path('change-password-with-old-password/', views.pass_change, name = "passchange"),
    path('change-password/', views.pass_change2, name = "passchange2"),
]