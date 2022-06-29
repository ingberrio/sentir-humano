from django.urls import path
from customers.views import InvoicePdfView, CustomerPdfView

app_name = 'customer'
urlpatterns = [
    path('admin/customers/customer/', CustomerPdfView.as_view(), name='credentialPDF'),
    path('admin/customers/invoice/', InvoicePdfView.as_view(), name='generatePDF')

]