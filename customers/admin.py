from django.contrib import admin
from .models import Customer

@admin.register(Customer)
class UserAdmin(admin.ModelAdmin):
    list_display = ["first_name", "phone", "person_id", "is_active", "membership_id"]
    search_fields = ["phone", "email"]
    exclude = ["password","last_login"]
    list_filter = ["age", "is_active"]
    list_per_page = 5
    