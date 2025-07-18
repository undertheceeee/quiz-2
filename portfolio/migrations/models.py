from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Project(models.Model):
    project_name = models.CharField(max_length=200)
    project_description = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.project_name

    class Portfolio(models.Model):
        project_name = models.CharField(max_length=200)
        project_description = models.TextField()
        created_at = models.DateTimeField(default=timezone.now)
        updated_at = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}'s Portfolio"

    class Meta:
        ordering = ('-created_at',)