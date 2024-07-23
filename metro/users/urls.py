from django.urls import path

from users import views

app_name = 'users'

urlpatterns = [
    path('', views.UsersListView.as_view(), name='users-list'),
    path('<int:pk>/update', views.UserUpdateView.as_view(), name='profile')
]
