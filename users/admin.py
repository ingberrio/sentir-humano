from django.contrib.admin import AdminSite
from django.utils.translation import gettext_lazy as _
from django.contrib import admin
from .models import NewUser
from . import models


@admin.register(NewUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'username', 'real_id', 'code_vs', 'phone', 'is_active')
    list_editable = ('username','real_id')
    search_fields = ('real_id', 'email')

