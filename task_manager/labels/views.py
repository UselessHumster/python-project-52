from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .models import Label


class LabelListView(LoginRequiredMixin, ListView):
    model = Label
    template_name = "labels/label_list.html"


class LabelCreateView(LoginRequiredMixin, CreateView):
    model = Label
    fields = ["name"]
    template_name = "labels/label_form.html"
    success_url = reverse_lazy("label_list")

    def form_valid(self, form):
        messages.success(self.request, "Метка успешно добавлена")
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form_title"] = "Создать метку"
        context["submit_cap"] = "Создать"
        return context


class LabelUpdateView(LoginRequiredMixin, UpdateView):
    model = Label
    fields = ["name"]
    template_name = "labels/label_form.html"
    success_url = reverse_lazy("label_list")

    def form_valid(self, form):
        messages.success(self.request, "Метка успешно изменена")
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form_title"] = "Обновление метки"
        context["submit_cap"] = "Изменить"
        return context


class LabelDeleteView(LoginRequiredMixin, DeleteView):
    model = Label
    template_name = "labels/label_confirm_delete.html"
    success_url = reverse_lazy("label_list")

    def post(self, request, *args, **kwargs):
        label = self.get_object()

        if label.tasks.exists():
            messages.error(
                self.request,
                "Невозможно удалить метку, потому что она используется",
            )
            return redirect("label_list")

        messages.success(self.request, "Метка успешно удалена")
        return super().post(request, *args, **kwargs)
