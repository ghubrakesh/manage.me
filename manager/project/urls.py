from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import projects, add, get, edit, delete, upload_file, delete_file


app_name = 'project'

urlpatterns = [
    path('', projects, name='projects'),
    path('add/', add, name='add'),
    path('<uuid:pk>/', get, name="project"),
    path('edit/<uuid:pk>/', edit, name="edit"),
    path('delete/<uuid:pk>/', delete, name="delete"),
    path('<uuid:pk>/upload_files/', upload_file, name="upload_file"),
    path('<uuid:project_id>/files/<uuid:pk>/delete/', delete_file , name="delete_file"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
