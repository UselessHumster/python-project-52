import django_filters
from django import forms
from django.contrib.auth import get_user_model

from labels.models import Label
from statuses.models import Status

from .models import Task

User = get_user_model()


class TaskFilter(django_filters.FilterSet):
    status = django_filters.ModelChoiceFilter(
        queryset=Status.objects.all(),
        label="Status",
    )

    executor = django_filters.ModelChoiceFilter(
        queryset=User.objects.all(),
        label="Executor",
    )

    labels = django_filters.ModelChoiceFilter(
        queryset=Label.objects.all(),
        label="Label",
        method="filter_by_label",
    )

    self_tasks = django_filters.BooleanFilter(
        label="Only my tasks",
        method="filter_self_tasks",
        widget=forms.CheckboxInput,
    )

    class Meta:
        model = Task
        fields = ["status", "executor", "labels", "self_tasks"]

    def filter_by_label(self, queryset, name, value):
        if value:
            return queryset.filter(labels=value)
        return queryset

    def filter_self_tasks(self, queryset, name, value):
        if value:
            return queryset.filter(author=self.request.user)
        return queryset