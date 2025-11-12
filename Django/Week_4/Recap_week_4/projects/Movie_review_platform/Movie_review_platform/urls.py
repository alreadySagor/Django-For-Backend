from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('genre/', include("genre.urls")),
    path('distributer/', include("distributer.urls")),
    path('profile/', include("profiles.urls")),
    path('user/', include("user.urls")),
    path('user_profile/', include("user_profile.urls")),
    path('review/', include("review_rating.urls")),
    path('movie/', include("movie.urls")),
]