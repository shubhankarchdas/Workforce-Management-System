from django.db import models
from organizations.models import Organization

class Project(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    active_flag = models.BooleanField(default=True)

    def __str__(self):
        return self.project_name
