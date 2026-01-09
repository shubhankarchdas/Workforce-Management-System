from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework import status

class OrganizationAPITest(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="admin", password="123")
        self.client.login(username="admin", password="123")

    def test_create_organization(self):
        self.client.force_authenticate(user=self.user)

        response = self.client.post(
            "/api/org/create/",
            {"name": "My Org"},
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
