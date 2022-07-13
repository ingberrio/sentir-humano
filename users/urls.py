from django.urls import re_path
from . import views

app_name = 'users' # So we can use it like: {% url 'users:user_login' %} on our template.
urlpatterns = [
    re_path(r'^login/$', views.user_login, name='user_login')
]