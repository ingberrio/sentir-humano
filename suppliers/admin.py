from django.contrib import admin
from .models import Service, Supplier

@admin.register(Supplier)
class UserAdmin(admin.ModelAdmin):
    list_display = ["specialty", "first_name", "last_name","phone", "city"]
    search_fields = ["phone", "email", "specialty", "phone"]
    exclude = ["password", "last_login"]
    list_filter = ["is_active", "city"]
    list_per_page = 10

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ["suppliers","name", "value_sh", "value"]
    search_fields = []
    readonly_fields = ('updatedAt',)
    exclude = ["last_login" ]
    list_filter = []
    list_per_page = 10