from django.contrib import admin
from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Настройки модели Пользователь
    для отображения в панели администратора."""

    list_display = ['full_name', 'email', 'address',]
    search_fields = ['full_name',]
    list_filter = ('full_name',)
