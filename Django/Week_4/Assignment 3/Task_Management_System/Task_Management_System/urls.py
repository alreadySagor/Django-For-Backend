from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.view_task, name = "view_task"),
    path('task/', include("task.urls")),
    path('category/', include("category.urls")),
    path('delete/<int:id>', views.delete_task, name = "delete_task"),
    path('edit/<int:id>', views.edit_task, name = "edit_task"),
]
