from django.test import TestCase
from django.contrib.auth.models import User
from organizations.models import Organization
from projects.models import Project
from attendance.models import Attendance
from datetime import date

class AttendanceModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="test", password="123")
        self.org = Organization.objects.create(
            name="Test Org",
            created_by=self.user
        )
        self.project = Project.objects.create(
            organization=self.org,
            project_name="Test Project",
            location="Delhi"
        )

    def test_unique_attendance_per_project_per_date(self):
        Attendance.objects.create(
            project=self.project,
            attendance_date=date.today(),
            present_count=5,
            created_by=self.user
        )

        with self.assertRaises(Exception):
            Attendance.objects.create(
                project=self.project,
                attendance_date=date.today(),  # same date
                present_count=6,
                created_by=self.user
            )
