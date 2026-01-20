from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .forms import UserCreateForm, UserUpdateForm


class UserListView(ListView):
    model = User
    template_name = "users/user_list.html"


class UserCreateView(CreateView):
    model = User
    form_class = UserCreateForm
    template_name = "users/user_form.html"
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Пользователь успешно зарегистрирован")
        return response


class UserUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = "users/user_form.html"
    success_url = reverse_lazy("user_list")

    def test_func(self):
        return self.request.user == self.get_object()

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Пользователь успешно обновлён")
        return response


class UserDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = User
    template_name = "users/user_confirm_delete.html"
    success_url = reverse_lazy("user_list")

    def test_func(self):
        return self.request.user == self.get_object()

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Пользователь успешно удалён")
        return super().delete(request, *args, **kwargs)




class UserLoginView(LoginView):
    template_name = "registration/login.html"

    def form_valid(self, form):
        messages.success(self.request, "Вы залогинены")
        return super().form_valid(form)