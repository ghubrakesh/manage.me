from django.urls import path
from .views import task, add, edit, delete

app_name = 'task'

urlpatterns = [
    path('add/', add, name="add"),
    path('<uuid:pk>/', task, name="task"),
    path('<uuid:pk>/edit', edit, name="edit"),
    path('<uuid:pk>/delete', delete, name="delete"),
]