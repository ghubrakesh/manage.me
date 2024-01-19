import uuid
from django.db import models

from account.models import User
from project.models import Project


class TodoList(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    project = models.ForeignKey(Project, related_name='todolists', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name='todolists', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    