from django.urls import path
from . import views
urlpatterns = [
    # path('', views.home),
    path('', views.set_session),
    path('get/', views.get_cookie),
    path('get_session/', views.get_session),
    path('delete_cookie/', views.delete_cookie),
    path('delete_session/', views.delete_session),
]