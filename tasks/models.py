from django.db import models
from projects.models import Project
from employees.models import Employee

class Task(models.Model):
    STATUS_CHOICES = [
        ('TODO', 'Todo'),
        ('DONE', 'Done'),
    ]

    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(Employee, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    def __str__(self):
        return self.title
