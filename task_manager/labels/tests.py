from django.test import TestCase
from django.urls import reverse

from task_manager.statuses.models import Status
from task_manager.tasks.models import Task

from .models import Label

from django.contrib.auth import get_user_model

User = get_user_model()

class LabelCRUDTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="user",
            password="password123",
        )
        self.client.login(username="user", password="password123")

        self.label = Label.objects.create(name="Bug")

        self.status = Status.objects.create(name="New")

        self.task = Task.objects.create(
            name="Task 1",
            status=self.status,
            author=self.user,
        )
        self.task.labels.add(self.label)

    def test_label_create(self):
        response = self.client.post(
            reverse("label_create"),
            {"name": "Feature"},
        )
        self.assertEqual(Label.objects.count(), 2)
        self.assertRedirects(response, reverse("label_list"))

    def test_label_update(self):
        self.client.post(
            reverse("label_update", args=[self.label.id]),
            {"name": "Bugfix"},
        )
        self.label.refresh_from_db()
        self.assertEqual(self.label.name, "Bugfix")

    def test_label_delete_protected(self):
        self.client.post(reverse("label_delete", args=[self.label.id]))
        self.assertEqual(Label.objects.count(), 1)

    def test_label_delete_free(self):
        self.task.labels.clear()
        self.client.post(reverse("label_delete", args=[self.label.id]))
        self.assertEqual(Label.objects.count(), 0)
