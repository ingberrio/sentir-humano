from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.utils.translation import gettext_lazy as _


class Supplier(AbstractBaseUser):
    specialty = models.CharField("Especialidad", max_length=255, default='')
    first_name = models.CharField("Nombre especilista", max_length=255)
    last_name = models.CharField("Institucion", max_length=255)
    city = models.CharField("Ciudad", max_length=255, default='')
    email = models.EmailField(blank=True)
    phone = models.CharField("Telefono principal",max_length=20)
    phone_two = models.CharField("Telefono secundario", blank=True, max_length=20, default=' ')
    discount = models.CharField("Tarifa particular", blank=True, max_length=255, default=' ')
    address =  models.CharField("Direccion", blank=True, null=True, max_length=255)
    description = models.TextField("Notas", blank=True, null=True)
    createdAt = models.DateTimeField("Creado", auto_now_add=True)
    is_active = models.BooleanField('Activo',default=False)
    

    class Meta:
        verbose_name = _("Proveedores")
        verbose_name_plural = _("Proveedores")
        ordering = ['-id']
        
    USERNAME_FIELD = 'email'
    
    def __str__(self):
        cadena = self.specialty+" - "+self.first_name
        return cadena

class Service(AbstractBaseUser):
    username = None
    password = None
    name = models.CharField("Nombre subcategoria", max_length=255)
    suppliers = models.ForeignKey(Supplier, null=True, on_delete=models.SET_NULL, verbose_name='Servicios')
    value_sh = models.DecimalField("Valor SH.", blank=True, max_digits=10, decimal_places = 0, default='0')
    value = models.DecimalField("Valor particular", blank=True, max_digits=10, decimal_places = 0, default='0')
    about = models.TextField("Notas", blank=True, null=True)
    createdAt = models.DateTimeField("Creado", auto_now_add=True)
    updatedAt = models.DateTimeField("Actualizado", blank=True, auto_now_add=True)
    is_active = models.BooleanField('Activo',default=False)
    
    class Meta:
        verbose_name = _("Servicios")
        verbose_name_plural = _("Servicios")
    
    USERNAME_FIELD = 'name'
    REQUIRED_FIELDS = []
    
    def __str__(self):
        cadena = self.name+" - "+str(self.value_sh)+" - "+self.suppliers.first_name+" - "+self.suppliers.last_name
        return cadena