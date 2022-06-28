from django.conf.urls import url
from . import views
from customers.views import InvoicePdfView

app_name = 'costumers.invoice' # So we can use it like: {% url 'users:user_login' %} on our template.
urlpatterns = [
    url(r'^invoice/$', views.InvoicePdfView.as_view(), name='invoice')
]