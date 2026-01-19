from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from task_manager.statuses.models import Status

from .models import Task


class TaskCRUDTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="author",
            password="password123",
        )
        self.other_user = User.objects.create_user(
            username="executor",
            password="password123",
        )

        self.status = Status.objects.create(name="New")

        self.task = Task.objects.create(
            name="Test task",
            description="Description",
            status=self.status,
            author=self.user,
            executor=self.other_user,
        )

    def test_task_list_requires_login(self):
        response = self.client.get(reverse("task_list"))
        self.assertEqual(response.status_code, 302)

    def test_task_create(self):
        self.client.login(username="author", password="password123")

        response = self.client.post(
            reverse("task_create"),
            {
                "name": "New task",
                "description": "Desc",
                "status": self.status.id,
                "executor": self.other_user.id,
            },
        )

        self.assertEqual(Task.objects.count(), 2)
        self.assertRedirects(response, reverse("task_list"))

    def test_task_update(self):
        self.client.login(username="author", password="password123")

        response = self.client.post(
            reverse("task_update", args=[self.task.id]),
            {
                "name": "Updated",
                "description": "New desc",
                "status": self.status.id,
                "executor": self.other_user.id,
            },
        )

        self.task.refresh_from_db()
        self.assertEqual(self.task.name, "Updated")
        self.assertRedirects(response, reverse("task_list"))

    def test_task_delete_only_author(self):
        # не автор
        self.client.login(username="executor", password="password123")
        self.client.post(reverse("task_delete", args=[self.task.id]))
        self.assertEqual(Task.objects.count(), 1)

        # автор
        self.client.login(username="author", password="password123")
        self.client.post(reverse("task_delete", args=[self.task.id]))
        self.assertEqual(Task.objects.count(), 0)

    def test_filter_by_status(self):
        self.client.login(username="author", password="password123")

        response = self.client.get(
            reverse("task_list"),
            {"status": self.status.id},
        )

        self.assertContains(response, self.task.name)

    def test_filter_self_tasks(self):
        self.client.login(username="author", password="password123")

        response = self.client.get(
            reverse("task_list"),
            {"self_tasks": "on"},
        )

        self.assertContains(response, self.task.name)

        self.client.login(username="executor", password="password123")

        response = self.client.get(
            reverse("task_list"),
            {"self_tasks": "on"},
        )

        self.assertNotContains(response, self.task.name)
