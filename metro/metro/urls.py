from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls', namespace='main')),
    # path('post/', include('posts.urls', namespace='post')),
    path('user/', include('users.urls', namespace='user')),
]
