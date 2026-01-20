from django.shortcuts import render
from django.contrib import messages

from django.contrib.auth import logout
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect


def index(request):
    return render(request, "index.html")


class UserLoginView(LoginView):
    template_name = "registration/login.html"

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Вы залогинены")
        return response


class UserLogoutView(LogoutView):
    def post(self, request, *args, **kwargs):
        messages.success(request, "Вы разлогинены")
        logout(request)
        return redirect(self.get_success_url())