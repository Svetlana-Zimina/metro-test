from django.contrib import admin
from posts.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Настройки модели Посты
    для отображения в панели администратора."""

    list_display = ['pk', 'title', 'text', 'author', 'pub_date',]
    search_fields = ['title',]
    list_filter = ('pub_date',)
