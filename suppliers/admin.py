from django.contrib import admin
from .models import Supplier

@admin.register(Supplier)
class UserAdmin(admin.ModelAdmin):
    list_display = ('specialty', 'first_name', 'phone' )
    search_fields = ('phone', 'email')
    