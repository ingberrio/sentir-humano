from django.utils.translation import gettext_lazy as _
from django.contrib import admin
from django.urls import path
from home import views
from .models import Customer, Appointment, Invoice
import csv
from django.http import HttpResponse
from django.utils.html import format_html
from simple_history.admin import SimpleHistoryAdmin
from customers.views import InvoicePdfView, CustomerPdfView
from datetime import datetime
from django.contrib import messages

class ExportCsvMixin:
    def export_as_csv(self, request, queryset):

        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_as_csv.short_description = "Exportar a CSV"



@admin.register(Invoice)
class InvoiceAdmin(SimpleHistoryAdmin):
    
    list_display = ('customer', 'contribution_date', 'added_by', 'balance', 'status', 'generatePDF' )
    readonly_fields = ('get_value','contribution_date','added_by', 'buffer_full_payment' )
    fields = ('contribution_date', 'customer', 'pay_method','buffer_full_payment', 'full_payment', 'balance', 'status', 'added_by', 'notes')
    search_fields = ['customer__first_name', 'customer__person_id']
    list_filter = ('balance','contribution_date')
    
    
    def get_urls(self):
        urls = super(InvoiceAdmin, self).get_urls()
        custom_urls = [
            path('generatePDF/<int:pk>',  InvoicePdfView.as_view(), name='generatePDF' )
        ]
        return custom_urls + urls
    
    def generatePDF(self, obj):
        return format_html(
            "<a href='generatePDF/{}' class='btn btn-outline-danger float-right' >Exportat PDF</a>",
            (obj.id),
        )
    

    # Method that show the field value of costumer on innvoice
    
    @admin.display(ordering='customer__value', description='Total')
    def get_value(self, obj):
        return obj.customer.value

    # Method that create user on field added_by

    def save_form(self, request, form, change):
        obj = super().save_form(request, form, change)
        if not change:
            obj.added_by = request.user
        return obj

    # showing current user accounts appoiments
    
    def get_queryset(self, request):
        query = super(InvoiceAdmin, self).get_queryset(request)
        if request.user.is_superuser: # just using request.user attributes
            filtered_query = query.filter()
        else:
            filtered_query = query.filter(added_by=request.user.id)
        return filtered_query

@admin.register(Appointment)
class AppointmentAdmin(SimpleHistoryAdmin):
    
    list_editable = ['is_confirm', 'is_cancel']
    list_display = ["customer", "type_appointment",  "added_by", 'service',  "is_confirm", "is_cancel"]
    fields = ('start_date', 'added_by', 'customer', 'type_appointment', 'service','end_date', 'about', 'is_confirm', 'is_cancel')
    search_fields = ['customer__first_name', 'customer__person_id']
    readonly_fields = ('start_date','added_by')
    list_filter = ["start_date", "service", "added_by" ]
    exclude = ["password"]
    list_per_page = 10
    actions = ["generate_bill"]

    # Method that record added_by on user field

    def save_form(self, request, form, change):
        obj = super().save_form(request, form, change)
        now = datetime.today().date()
        start = obj.customer.endsAt.date()
        
        if start < now:
            messages.error(request, "Verifique la fecha de afiliación")
            return obj
        else:
            obj.added_by = request.user
            return obj

        
    # showing current user accounts appoiments
    
    def get_queryset(self, request):
        query = super(AppointmentAdmin, self).get_queryset(request)
        if request.user.is_superuser: # just using request.user attributes
            filtered_query = query.filter()
        else:
            filtered_query = query.filter(added_by=request.user.id)
        return filtered_query
    
        
@admin.register(Customer)
class UserAdmin(SimpleHistoryAdmin, ExportCsvMixin):
    
    list_editable = ["is_active"]
    list_display = ["first_name", "phone", "person_id", "is_active", "membership_id", "collector", "status_membership", "gener", "is_collector", 'credentialPDF']
    search_fields = ["phone", "email", "person_id", "first_name", "last_name"]
    list_display_links = ["first_name", "person_id"]
    exclude = ('password','last_login')
    readonly_fields = ('value', 'start_date')
    list_filter = ["age", "is_active", "membership_id", "is_collector", 'status_membership']
    list_per_page = 10
    actions = ["export_as_csv"]

    def get_urls(self):
        urls = super(UserAdmin, self).get_urls()
        custom_urls = [
            path('credentialPDF/<int:pk>',  CustomerPdfView.as_view(), name='credentialPDF' )
        ]
        return custom_urls + urls
    
    def credentialPDF(self, obj):
        return format_html(
            "<a href='credentialPDF/{}' class='btn btn-outline-danger'>Carnet</a>",
            (obj.id),
        )
          
    fieldsets = (
        (None, {
            'fields': ('start_date','first_name','last_name','person_id', 'age','status_membership', 'phone', 'phone_contact',  
            'asesor_id', 'endsAt', 'description', 'is_active', 'is_main')
            
        }),
        ('Cobro',{
            'classes': ('collapse',),
            'fields': ([ 'creator_by','membership_id','payment_descount', 'value', 'way_to_pay', 'collector','is_collector','createdAt','city_pay', 'address_to_pay']),
        }),
        ('Opciones avanzadas', {
            'classes': ('collapse',),
            'fields': ([ 'email', 'birth_day','gener', 'city', 'neigbord', 'address']),
        }),
        ('Afiliados', {
            'classes': ('collapse',),
            'fields': ([ 'affiliate_one_customer', 'affiliate_two_customer',
                        'affiliate_three_customer', 'affiliate_four_customer',
                        'affiliate_five_customer', 'affiliate_six_customer',
                        'affiliate_seven_customer'
            ]),
        }),
    )

    def creator_by(self, obj):
        return format_html('<a href={}>URL</a>', obj.url)

    # Method that create user on field added_by
    def save_form(self, request, form, change):
        obj = super().save_form(request, form, change)
        if not change:
            obj.creator_by = request.user
            obj.collector = request.user
            obj.asesor_id = request.user
        return obj
    
    # showing current user accounts appoiments
    def get_queryset(self, request):
        query = super(UserAdmin, self).get_queryset(request)
        if request.user.is_superuser: # just using request.user attributes
            filtered_query = query.filter()
        else:
            filtered_query = query.filter(creator_by=request.user.id)
        return filtered_query

    # Just read if not a superuser
    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return super(UserAdmin, self).get_readonly_fields(request, obj)
        else:
            return ('collector', 'status_membership', 'creator_by', 'start_date', 'asesor_id')

    
    
