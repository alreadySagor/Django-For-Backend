from django.urls import path
from . import views
urlpatterns = [
    path('register/', views.registration, name = "register"),
    # path('login/', views.user_login, name = "login"),
    path('login/', views.BuyerLoginView.as_view(), name = "login"),
    path('logout/', views.user_logout, name = "logout"),
    path('profile/', views.profile, name = "profile"),
    path('profile/edit/', views.edit_profile, name = "edit_profile"),
    path('profile/edit/change-password/', views.pass_change, name = "pass_change"),
    path('buy-car/<int:id>/', views.buy_car, name = "buy_car"),
]