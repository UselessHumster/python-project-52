from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

User = get_user_model()


class UserCRUDTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='password123',
            first_name='Test',
            last_name='User'
        )

    def test_user_create(self):
        response = self.client.post(
            reverse("user_create"),
            {
                "username": "newuser",
                "first_name": "New",
                "last_name": "User",
                "password1": "StrongPass123!",
                "password2": "StrongPass123!",
            },
        )
        self.assertEqual(User.objects.count(), 2)
        self.assertRedirects(response, reverse("login"))

    def test_user_update(self):
        self.client.login(username="testuser", password="password123")

        response = self.client.post(
            reverse("user_update", args=[self.user.id]),
            {
                "username": self.user.username,
                "first_name": "Updated",
                "last_name": "Name",
                'password1': self.user.password,
                'password2': self.user.password,
            },
        )

        self.user.refresh_from_db()
        self.assertEqual(self.user.first_name, "Updated")
        self.assertRedirects(response, reverse("user_list"))

    def test_user_delete(self):
        self.client.login(username="testuser", password="password123")

        response = self.client.post(
            reverse("user_delete", args=[self.user.id]),
        )

        self.assertEqual(User.objects.count(), 0)
        self.assertRedirects(response, reverse("user_list"))
