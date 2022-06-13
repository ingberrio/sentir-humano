from attr import fields
from django.contrib import admin
from .models import Customer, Appointment
import csv
from django.http import HttpResponse

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

    export_as_csv.short_description = "Exportar"

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_editable = ['is_confirm', 'is_cancel']
    list_display = ["customer", "type_appointment",  "added_by", 'supplier',  "is_confirm", "is_cancel"]
    search_fields = ['customer__first_name', 'customer__person_id']
    readonly_fields = ('start_date','added_by')
    list_filter = ["start_date", "supplier", "added_by" ]
    exclude = ["password"]
    list_per_page = 10

    # Method that create user on field added_by

    def save_form(self, request, form, change):
        obj = super().save_form(request, form, change)
        if not change:
            obj.added_by = request.user
        return obj
        
@admin.register(Customer)
class UserAdmin(admin.ModelAdmin, ExportCsvMixin):
    
    readonly_fields = ('start_date',)
    list_editable = ["is_active"]
    list_display = ["first_name", "phone", "person_id", "is_active", "membership_id"]
    search_fields = ["phone", "email", "person_id"]
    list_display_links = ["first_name", "person_id"]
    exclude = ["password","last_login"]
    list_filter = ["age", "is_active"]
    list_per_page = 10
    actions = ["export_as_csv"]

    fieldsets = (
        (None, {
            'fields': ('start_date','first_name','last_name','person_id', 'phone', 
            'membership_id', 'asesor_id', 'way_to_pay','value',  
            'description', 'is_active')
        }),
        ('Opciones avanzadas', {
            'classes': ('collapse',),
            'fields': ([ 'email', 'age', 'city', 'neigbord', 'address']),
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
    