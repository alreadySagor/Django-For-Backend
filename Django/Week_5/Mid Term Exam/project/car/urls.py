from django.urls import path
from . import views
urlpatterns = [
    path('add-car/', views.add_car, name = "add_car"),
    path('details/<int:id>/', views.car_details, name = "car_details"),
]