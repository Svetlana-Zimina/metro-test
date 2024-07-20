from django.urls import path

from users import views

app_name = 'users'

urlpatterns = [
    path('', views.UsersListView.as_view(), name='users-list'),
    path('<str:full_name>/', views.ProfileView.as_view(), name='profile'),
]
