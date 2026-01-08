from django.contrib import admin
# include ke import korar karon hocche link http://127.0.0.1:8000/first_app/courses/ show korbe
from django.urls import path, include

# Eita dite chaile -- > path('contact/', contact)
# from views import contact
# (eita dile path('contact/', views.contact) dite hobe)
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    # Blank path (jodi kew blank thake)
    path("", views.homepage),
    # first_app er por ami chai, home, about, contact egula jeno link er moddhe add hoy, tai first_app(ba others app) er link gula ekhane include kore dite hobe
    path("first_app/", include("first_app.urls")),
    # path("second_app/", include("second_app.urls")),
    path('contact/', views.contact),
]
