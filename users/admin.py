from django.contrib.admin import AdminSite
from django.utils.translation import gettext_lazy as _
from django.contrib import admin
from .models import NewUser
from . import models


@admin.register(NewUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ["email", "real_id", "phone", "is_active"]
    list_editable = ["real_id"]
    search_fields = ["real_id", "phone", "email"]
    list_filter = ["is_active"]
    list_per_page = 5

