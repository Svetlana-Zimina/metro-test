from django.views.generic import TemplateView

from users.models import User
from posts.models import Post


class IndexView(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная'
        context['posts'] = Post.objects.all()
        context['users'] = User.objects.all()
        return context
