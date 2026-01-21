from django import forms

from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["name", "description", "status", "executor", "labels"]
        widgets = {
            "labels": forms.SelectMultiple(attrs={"class": "form-control"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["executor"].empty_label = "Исполнитель"
        self.fields["status"].empty_label = "Статус"