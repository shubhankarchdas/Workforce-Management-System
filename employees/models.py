from django.db import models
from organizations.models import Organization
from projects.models import Project

class Employee(models.Model):
    ROLE_CHOICES = [
        ('OWNER', 'Owner'),
        ('MANAGER', 'Manager'),
        ('MEMBER', 'Member'),
    ]

    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    projects = models.ManyToManyField(Project, blank=True)

    def __str__(self):
        return self.name
