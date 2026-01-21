from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class UserCreateForm(UserCreationForm):
    username = forms.CharField(
        label="Имя пользователя",
        widget=forms.TextInput(
            attrs={"placeholder": "Имя пользователя"}
        ),
        help_text='Обязательно. Не более 150 символов. '
                  'Только буквы, цифры и @/./+/-/_')
    password1 = forms.CharField(
        label="Пароль",
        help_text='Ваш пароль должен содержать как минимум 3 символа.',
        widget=forms.PasswordInput(
            attrs={"placeholder": "Пароль"}
        ),
    )
    password2 = forms.CharField(
        label="Подтверждение пароля",
        help_text='Для подтверждения введите, пожалуйста, пароль ещё раз.',
        widget=forms.PasswordInput,
    )

    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "password1", "password2")
        labels = {
            "username": "Имя пользователя",
            "first_name": "Имя",
            "last_name": "Фамилия",
            "password1": "Пароль",
            "password2": "Подтверждение пароля",

        }


class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(
        label="Имя пользователя",
        widget=forms.TextInput(
            attrs={"placeholder": "Имя пользователя"}
        ),
        help_text='Обязательно. Не более 150 символов. '
                  'Только буквы, цифры и @/./+/-/_')
    password1 = forms.CharField(
        label="Пароль",
        help_text='Ваш пароль должен содержать как минимум 3 символа.',
        widget=forms.PasswordInput(
            attrs={"placeholder": "Пароль"}
        ),
    )
    password2 = forms.CharField(
        label="Подтверждение пароля",
        help_text='Для подтверждения введите, пожалуйста, пароль ещё раз.',
        widget=forms.PasswordInput,
    )

    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "password1", "password2")
        labels = {
            "username": "Имя пользователя",
            "first_name": "Имя",
            "last_name": "Фамилия",
            "password1": "Пароль",
            "password2": "Подтверждение пароля",

        }
