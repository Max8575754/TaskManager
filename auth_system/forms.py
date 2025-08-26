from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'form-control form-control-lg bg-dark text-light border-secondary',
            'placeholder': '👤 Введіть логін'
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control form-control-lg bg-dark text-light border-secondary',
            'placeholder': '🔒 Введіть пароль'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control form-control-lg bg-dark text-light border-secondary',
            'placeholder': '🔒 Підтвердіть пароль'
        })


class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(
        label="👤 Логін",
        widget=forms.TextInput(attrs={
            "class": "form-control form-control-lg bg-dark text-light border-secondary",
            "placeholder": "Введіть свій логін",
            "aria-label": "Логін"
        })
    )
    password = forms.CharField(
        label="🔒 Пароль",
        widget=forms.PasswordInput(attrs={
            "class": "form-control form-control-lg bg-dark text-light border-secondary",
            "placeholder": "Введіть свій пароль",
            "aria-label": "Пароль"
        })
    )