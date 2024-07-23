from django.views.generic import ListView, UpdateView

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


class UserUpdateView(UpdateView):

    model = User
    template_name = 'users/user_profile.html'

    fields = [ 
        'full_name',
        'email',
        'address'
    ]
    success_url = '/user'
