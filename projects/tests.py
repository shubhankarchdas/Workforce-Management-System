from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from organizations.models import Organization
from employees.models import Employee
from rest_framework import status

class PermissionTest(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="111", password="123")
        self.org = Organization.objects.create(name="Org", created_by=self.user)

        self.employee = Employee.objects.create(
            name="Member",
            phone="111",
            role="MEMBER",
            organization=self.org
        )

        self.client.force_authenticate(user=self.user)

    def test_member_cannot_create_project(self):
        response = self.client.post(
            "/api/project/create/",
            {
                "organization": self.org.id,
                "project_name": "X",
                "location": "Delhi"
            }
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
