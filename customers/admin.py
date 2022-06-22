from django.utils.translation import gettext_lazy as _
from django.contrib import admin
from .models import Customer, Appointment, Invoice
import csv
from django.http import HttpResponse
from django.utils.html import format_html

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
class InvoiceAdmin(admin.ModelAdmin):
    

    list_display = ('customer', 'contribution_date', 'added_by', 'balance', 'status')
    readonly_fields = ('get_value','contribution_date','added_by', 'balance' )
    fields = ('contribution_date', 'customer', 'pay_method', 'full_payment', 'balance', 'status', 'added_by', 'notes')
    search_fields = ['customer__first_name', 'customer__person_id']

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
class AppointmentAdmin(admin.ModelAdmin):
    
    list_editable = ['is_confirm', 'is_cancel']
    list_display = ["customer", "type_appointment",  "added_by", 'supplier',  "is_confirm", "is_cancel"]
    fields = ('start_date', 'added_by', 'customer', 'type_appointment', 'supplier','end_date', 'about', 'is_confirm', 'is_cancel')
    search_fields = ['customer__first_name', 'customer__person_id']
    readonly_fields = ('start_date','added_by')
    list_filter = ["start_date", "supplier", "added_by" ]
    exclude = ["password"]
    list_per_page = 10
    actions = ["generate_bill"]

    # Method that create user on field added_by

    def save_form(self, request, form, change):
        obj = super().save_form(request, form, change)
        if not change:
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
class UserAdmin(admin.ModelAdmin, ExportCsvMixin):
    
    list_editable = ["is_active"]
    list_display = ["first_name", "phone", "person_id", "is_active", "membership_id", 'status_membership', 'gener', 'is_collector']
    search_fields = ["phone", "email", "person_id"]
    list_display_links = ["first_name", "person_id"]
    exclude = ('password','last_login')
    readonly_fields = ('value',)
    list_filter = ["age", "is_active", "membership_id", "is_collector" ]
    list_per_page = 10
    actions = ["export_as_csv"]
          
    fieldsets = (
        (None, {
            'fields': ('start_date','first_name','last_name','person_id', 'age','status_membership', 'phone', 
            'asesor_id', 'endsAt', 'description', 'is_active', 'is_main')
            
        }),
        ('Cobro',{
            'classes': ('collapse',),
            'fields': ([ 'creator_by','membership_id', 'way_to_pay','value', 'collector','is_collector','createdAt', 'address_to_pay']),
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
            return ('collector', 'status_membership', 'creator_by')

    
    
