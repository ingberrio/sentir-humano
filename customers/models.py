from datetime import datetime
from django.contrib.admin.widgets import AdminDateWidget
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from memberships.models import Membership
from suppliers.models import Supplier
from users.models import NewUser
from django.utils import timezone
from django.conf import settings
from django.utils.translation import gettext_lazy as _

class Customer(AbstractBaseUser, models.Model):
    
    PAY_CHOICES = [
        ('1', 'Contado'),
        ('2', 'Quincenal'),
        ('3', 'Mensual'),
        ('4', 'Anual'),
    ]
    
    first_name = models.CharField("Nombres", max_length=255)
    last_name = models.CharField("Apellidos", max_length=255)
    person_id = models.CharField("Cedula", max_length=20, default=' ')
    membership_id = models.ForeignKey(Membership, null=True, on_delete=models.SET_NULL, verbose_name='Membresia')
    asesor_id = models.ForeignKey(NewUser, null=True, blank=True,  on_delete=models.SET_NULL, verbose_name='Asesor encargado', default='2')
    way_to_pay = models.CharField("Tipo de pago", null=True, max_length=255, choices=PAY_CHOICES)
    start_date = models.DateTimeField("Fecha de inicio", null=True, blank=True, default=datetime.now())
    value = models.CharField("Valor", null=True, blank=True, max_length=10)
    password = models.CharField("Password", max_length=255)
    affiliate_one_customer = models.ForeignKey("self", related_name='one', null=True, blank=True,  on_delete=models.SET_NULL, verbose_name='Afiliado Uno')
    affiliate_two_customer = models.ForeignKey("self", related_name='two', null=True, blank=True,  on_delete=models.SET_NULL, verbose_name='Afiliados Dos')
    affiliate_three_customer = models.ForeignKey("self", related_name='three', null=True, blank=True,  on_delete=models.SET_NULL, verbose_name='Afiliados Tres')
    affiliate_four_customer = models.ForeignKey("self", related_name='four', null=True, blank=True,  on_delete=models.SET_NULL, verbose_name='Afiliados Cuatro')
    affiliate_five_customer = models.ForeignKey("self", related_name='five', null=True, blank=True,  on_delete=models.SET_NULL, verbose_name='Afiliado Cinco')
    affiliate_six_customer = models.ForeignKey("self", related_name='six', null=True, blank=True,  on_delete=models.SET_NULL, verbose_name='Afiliado Seis')
    affiliate_seven_customer = models.ForeignKey("self", related_name='seven', null=True, blank=True,  on_delete=models.SET_NULL, verbose_name='Afiliado Siete')
    email = models.EmailField(blank=True)
    age = models.PositiveIntegerField("Edad", blank=True, null=True)
    city = models.CharField("Ciudad", blank=True, max_length=20, default=' ')
    neigbord = models.CharField("Barrio", blank=True, max_length=20, default=' ')
    phone = models.CharField("Telefono", blank=True, max_length=20)
    address =  models.CharField("Dirección", blank=True, null=True, max_length=255)
    description = models.TextField("Notas", blank=True, null=True)
    createdAt = models.DateTimeField("Created At", auto_now_add=True)
    is_active = models.BooleanField("Activo", default=False)

    class Meta:
        verbose_name = _("Clientes")
        verbose_name_plural = _("Clientes")
    
    USERNAME_FIELD = 'email'

    def save(self, *args, **kwargs):
        if self.person_id == "Sentir Humanos's App":
            return # Sentir shall never have him own App!
        else:
            super().save(*args, **kwargs) 

    def __str__(self):
        return self.person_id

class Appointment(models.Model):
    
    APPOIMENT_CHOICES = [
        ('1', 'Tipo 1'),
        ('2', 'Tipo 2'),
        ('3', 'Tipo 3'),
    ]
    start_date = models.DateTimeField("Inicio solicitud", default=timezone.now)
    type_appointment = models.CharField("Tipo de cita", max_length=255, choices=APPOIMENT_CHOICES)
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL, verbose_name='Cliente')
    supplier = models.ForeignKey(Supplier, null=True, on_delete=models.SET_NULL, verbose_name='Especialidad')
    end_date = models.DateTimeField("Fecha finalizacion", null=True, blank=True)
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, verbose_name="Creado por", blank=True)
    about = models.TextField("Observaciones", max_length=500, blank=True)
    is_confirm = models.BooleanField("Confirmada", default=False)
    is_cancel = models.BooleanField("Cancelada", default=False)

    class Meta:
        verbose_name = _("Citas")
        verbose_name_plural = _("Citas")
    
    def __str__(self):
        return self.type_appointment
