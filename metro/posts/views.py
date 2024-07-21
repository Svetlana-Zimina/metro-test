from django.views.generic import ListView

from posts.models import Post


class PostsListView(ListView):
    """Представление для получения списка постов."""

    model = Post
    queryset = Post.objects.all()
    template_name = 'posts/posts_list.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Посты'
        return context
