from django.urls import path
from .views import add, todolist, edit, delete

app_name = 'todolist'

urlpatterns = [
    path('add-todo/', add, name='add-todo'),
    path('<uuid:pk>/', todolist, name="todolist"),
    path('<uuid:pk>/edit/', edit, name='edit'),
    path('<uuid:pk>/delete/', delete, name='delete'),
]