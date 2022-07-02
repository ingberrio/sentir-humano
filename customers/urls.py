from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.contrib import admin
from customers.views import InvoicePdfView, CustomerPdfView


app_name = 'customer'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin/customers/customer/', CustomerPdfView.as_view(), name='credentialPDF'),
    path('admin/customers/invoice/', InvoicePdfView.as_view(), name='generatePDF')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)