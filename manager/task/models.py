import uuid
from django.db import models

from account.models import User
from project.models import Project
from todolist.models import TodoList

class Task(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    is_done = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, related_name='tasks', on_delete=models.CASCADE)
    project = models.ForeignKey(Project,related_name='tasks', on_delete=models.CASCADE)
    todolist = models.ForeignKey(TodoList,related_name='tasks', on_delete=models.CASCADE)

    def __str__(self):
        return self.name