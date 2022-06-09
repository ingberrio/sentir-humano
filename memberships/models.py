from django.db import models
from django.utils.translation import gettext_lazy as _


class Membership(models.Model):
    
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=10)
    description = models.TextField(max_length=255)
    is_active = models.BooleanField("Activo", default=False)

    class Meta:
        verbose_name = _("Membresia")
        verbose_name_plural = _("Membresia")
    
    def __str__(self):
        return self.name