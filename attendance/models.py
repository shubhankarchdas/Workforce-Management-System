from django.db import models
from django.contrib.auth.models import User
from projects.models import Project

class Attendance(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    attendance_date = models.DateField()
    present_count = models.PositiveIntegerField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('project', 'attendance_date')

    def __str__(self):
        return f"{self.project} - {self.attendance_date}"
