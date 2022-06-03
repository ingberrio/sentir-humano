from django.db import models


class Membership(models.Model):
    
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=10)
    description = models.TextField(max_length=255)
    is_active = models.BooleanField("Activo", default=False)
    
    def __str__(self):
        return self.name