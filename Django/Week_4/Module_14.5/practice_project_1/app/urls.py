from django.urls import path
from . import views
urlpatterns = [
    path('', views.djangoForm, name = "homepage"),
    path('model-form', views.modelForm, name = "modelform"),
]