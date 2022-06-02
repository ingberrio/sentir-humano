from django.contrib import admin
from .models import Customer

@admin.register(Customer)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'phone')
    search_fields = ('phone', 'email')
    