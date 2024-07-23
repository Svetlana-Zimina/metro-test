from django import forms
from users.models import User


class UserForm(forms.ModelForm):
    """Форма на основе модели Пользователь."""

    class Meta:
        model = User
        fields = ['full_name', 'email', 'address',]
