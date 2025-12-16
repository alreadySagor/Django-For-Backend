from django.urls import path
from . import views
urlpatterns = [
    # path('add-car/', views.add_car, name = "add_car"),
    path('add-car/', views.AddCarCreateView.as_view(), name = "add_car"),
    # path('details/<int:id>/', views.car_details, name = "car_details"),
    path('details/<int:id>/', views.DetailsCarView.as_view(), name = "car_details"),
]