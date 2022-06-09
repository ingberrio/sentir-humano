from django.contrib import admin
from .models import Customer, Appointment

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ["added_by", "type_appointment", "customer", 'supplier', "start_date", "is_confirm", "is_cancel"]
    search_fields = ['customer__first_name', 'customer__person_id']
    list_filter = ["start_date", "supplier", "added_by" ]
    exclude = ["password"]
    list_per_page = 10

@admin.register(Customer)
class UserAdmin(admin.ModelAdmin):
    list_display = ["first_name", "phone", "person_id", "is_active", "membership_id", "person_id"]
    search_fields = ["phone", "email", "person_id"]
    exclude = ["password","last_login"]
    list_filter = ["age", "is_active"]
    list_per_page = 10
    