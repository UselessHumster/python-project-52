from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import Status


class StatusCRUDTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="password123",
        )
        self.status = Status.objects.create(name="New")

    def test_status_list_requires_login(self):
        response = self.client.get(reverse("status_list"))
        self.assertEqual(response.status_code, 302)

    def test_status_create(self):
        self.client.login(username="testuser", password="password123")

        response = self.client.post(
            reverse("status_create"),
            {"name": "In progress"},
        )

        self.assertEqual(Status.objects.count(), 2)
        self.assertRedirects(response, reverse("status_list"))

    def test_status_update(self):
        self.client.login(username="testuser", password="password123")

        response = self.client.post(
            reverse("status_update", args=[self.status.id]),
            {"name": "Updated"},
        )

        self.status.refresh_from_db()
        self.assertEqual(self.status.name, "Updated")
        self.assertRedirects(response, reverse("status_list"))

    def test_status_delete(self):
        self.client.login(username="testuser", password="password123")

        response = self.client.post(
            reverse("status_delete", args=[self.status.id]),
        )

        self.assertEqual(Status.objects.count(), 0)
        self.assertRedirects(response, reverse("status_list"))
