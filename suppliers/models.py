from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class Supplier(AbstractBaseUser):
    specialty = models.CharField("Especialidad", max_length=255, default='')
    first_name = models.CharField("Nombre especilista", max_length=255)
    last_name = models.CharField("Institucion", max_length=255)
    city = models.CharField("Ciudad", max_length=255, default='')
    email = models.EmailField()
    phone = models.CharField("Telefono principal",max_length=20)
    phone_two = models.CharField("Telefono secundario",max_length=20)
    discount = models.CharField("Descuento", max_length=255, default=' ')
    address =  models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    createdAt = models.DateTimeField("Creado", auto_now_add=True)
    is_active = models.BooleanField('Activo',default=False)
    

    USERNAME_FIELD = 'email'
    
    def __str__(self):
        return self.first_name