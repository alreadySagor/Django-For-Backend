from django.urls import path
# from first_app.views import home
# from first_app import views # eita korle path er moddhe path('', views.home) dite hobe
from . import views
urlpatterns = [
    path('', views.home),
]
