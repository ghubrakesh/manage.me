from django.urls import path
from .views import projects, add, get, edit, delete


app_name = 'project'

urlpatterns = [
    path('', projects, name='projects'),
    path('add/', add, name='add'),
    path('<uuid:pk>/', get, name="project"),
    path('edit/<uuid:pk>/', edit, name="edit"),
    path('delete/<uuid:pk>/', delete, name="delete"),
    
]