from django.urls import path
from customers.views import InvoicePdfView, CustomerPdfView
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'customer'
urlpatterns = [
    path('admin/customers/customer/', views.CustomerPdfView.as_view(), name='credentialPDF'),
    path('admin/customers/invoice/', views.InvoicePdfView.as_view(), name='generatePDF')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)