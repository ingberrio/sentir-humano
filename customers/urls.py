from django.urls import path
from customers.views import InvoicePdfView, CustomerPdfView
from . import views

app_name = 'customer'
urlpatterns = [
    path('admin/customers/customer/', views.CustomerPdfView.as_view(), name='credentialPDF'),
    path('admin/customers/invoice/', views.InvoicePdfView.as_view(), name='generatePDF')

]