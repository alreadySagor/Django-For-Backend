from django.urls import path
from .import views
urlpatterns = [
    path('', views.home, name = "homepage"),
    path('signup/', views.user_signup, name = "signup"),
    path('login/', views.user_login, name = "login"),
    path('profile/', views.profile, name = "profile"),
    path('change-password/', views.pass_change, name = "pass_change"),
    path('change-password-without-old-password/', views.pass_change2, name = "pass_change2"),
    path('logout/', views.user_logout, name = "logout"),
]