from django.views.generic import DetailView, ListView

from users.models import User


class UsersListView(ListView):
    """Представление для получения списка пользователей."""

    model = User
    queryset = User.objects.all().order_by('full_name')
    template_name = 'users/users_list.html'
    context_object_name = 'users'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Пользователи'
        return context


class ProfileView(DetailView):

    template_name = 'users/user_profile.html'
    str_url_kwarg = 'full_name'
    context_object_name = 'users'

    def get_object(self, queryset=None):
        user = User.objects.get(full_name=self.kwargs.get(self.str_url_kwarg))
        return user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.object.full_name
        return context
