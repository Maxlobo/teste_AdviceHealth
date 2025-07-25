from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    """Model representing a task."""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """String representation of the Task model."""
        return self.title