from django.conf.urls import url
from . import views

app_name = 'users' # So we can use it like: {% url 'users:user_login' %} on our template.
urlpatterns = [
    url(r'^login/$', views.user_login, name='user_login')
]