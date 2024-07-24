from django.views.generic import TemplateView

from posts.models import Post
from users.models import User


class IndexView(TemplateView):
    """Представление для отображения главной страницы."""

    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная'
        context['posts'] = Post.objects.all()
        context['users'] = User.objects.all()
        return context
