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


PAY_CHOICES = [
        ('1', 'Contado'),
        ('2', 'Quincenal'),
        ('3', 'Mensual'),
        ('4', 'Anual'),
]

STATUS = [
        ('DIGITADO', 'DIGITADO'),
        ('CONTABILIZADO', 'CONTABILIZADO'),
        ('REVISADO', 'REVISADO'),
]

PAY_METHOD = [
        ('BANCOLOMBIA', 'BANCOLOMBIA'),
        ('BANCO DE BOG.', 'BANCO DE BOG.'),
        ('DAVIVIENDA', 'DAVIVIENDA'),
        ('EFECTIVO', 'EFECTIVO'),
        ('DATAFONO', 'DATAFONO'),
        ('OTRO', 'OTRO')
]

STATUS_MEMBERSHIP =[
    ('COBRO', 'COBRO'),
    ('PAGO', 'PAGO'),
    ('INCONVENIENTE', 'INCONVENIENTE'),
    ('INACTIVO', 'INCATIVO')
]

GENER = [
    ('FEMENINO', 'FEMENINO'),
    ('MASCULINO', 'MASCULINO'),
    ('OTRO', 'OTRO'),
]
class Customer(AbstractBaseUser, models.Model):
    #General section
    first_name = models.CharField("Nombres", max_length=255)
    last_name = models.CharField("Apellidos", max_length=255)
    person_id = models.CharField("Cedula", max_length=20, default=' ', unique=True)
    membership_id = models.ForeignKey(Membership, null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Membresia')
    asesor_id = models.ForeignKey(NewUser, null=True, blank=True,  on_delete=models.SET_NULL, verbose_name='Asesor encargado', default='2')
    collector = models.ForeignKey(NewUser, related_name='collector', null=True, blank=True,  on_delete=models.SET_NULL, verbose_name='Cobrador')
    is_collector = models.BooleanField("Cobro RF.", default=False)
    way_to_pay = models.CharField("Tipo de pago", blank=True, null=True, max_length=255, choices=PAY_CHOICES)
    start_date = models.DateTimeField("Fecha de Suscripcion", null=True, blank=True, default=datetime.now())
    value = models.FloatField("Valor", null=True, blank=True, max_length=10)
    password = models.CharField("Password", max_length=255)
    address_to_pay =  models.CharField("Direccion para cobrar", blank=True, null=True, max_length=255)
    
    #Afiliates section
    affiliate_one_customer = models.ForeignKey("self", related_name='one', null=True, blank=True,  on_delete=models.SET_NULL, verbose_name='Afiliado Uno')
    affiliate_two_customer = models.ForeignKey("self", related_name='two', null=True, blank=True,  on_delete=models.SET_NULL, verbose_name='Afiliado Dos')
    affiliate_three_customer = models.ForeignKey("self", related_name='three', null=True, blank=True,  on_delete=models.SET_NULL, verbose_name='Afiliado Tres')
    affiliate_four_customer = models.ForeignKey("self", related_name='four', null=True, blank=True,  on_delete=models.SET_NULL, verbose_name='Afiliado Cuatro')
    affiliate_five_customer = models.ForeignKey("self", related_name='five', null=True, blank=True,  on_delete=models.SET_NULL, verbose_name='Afiliado Cinco')
    affiliate_six_customer = models.ForeignKey("self", related_name='six', null=True, blank=True,  on_delete=models.SET_NULL, verbose_name='Afiliado Seis')
    affiliate_seven_customer = models.ForeignKey("self", related_name='seven', null=True, blank=True,  on_delete=models.SET_NULL, verbose_name='Afiliado Siete')
    
    #Advance section
    email = models.EmailField(blank=True)
    birth_day = models.DateField('Fecha de nacimiento', blank=True, null=True)
    age = models.PositiveIntegerField("Edad", blank=True, null=True)
    city = models.CharField("Ciudad", blank=True, max_length=20, default=' ')
    neigbord = models.CharField("Barrio", blank=True, max_length=20, default=' ')
    phone = models.CharField("Telefono", blank=True, max_length=20)
    address =  models.CharField("Dirección", blank=True, null=True, max_length=255)
    creator_by = models.ForeignKey(NewUser, related_name='created_by', null=True, blank=True,  on_delete=models.SET_NULL, verbose_name='Creado por')
    description = models.TextField("Notas", blank=True, null=True)
    createdAt = models.DateTimeField("Inicio Cobro",blank=True, null=True)
    endsAt = models.DateTimeField('Finalizacion', blank=True, null=True)
    is_active = models.BooleanField("Activo", default=False)
    is_main = models.BooleanField("Titular", default=False)
    status_membership = models.CharField('Estado', choices=STATUS_MEMBERSHIP, default='DIGITADO', max_length=100)
    gener = models.CharField('Genero', choices=GENER, blank=True, default= ' ', max_length=100)
    
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
        cadena="C.C: "+self.person_id+" - "+self.first_name
        return cadena

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
    end_date = models.DateTimeField("Fecha cita", null=True, blank=True)
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, verbose_name="Creado por", blank=True)
    about = models.TextField("Observaciones", max_length=500, blank=True)
    is_confirm = models.BooleanField("Confirmada", default=False)
    is_cancel = models.BooleanField("Cancelada", default=False)

    class Meta:
        verbose_name = _("Citas")
        verbose_name_plural = _("Citas")
    
    def __str__(self):
        return self.type_appointment

class Invoice(models.Model):
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL, verbose_name='Cliente')
    contribution_date = models.DateTimeField("Fecha de aporte", default=timezone.now)
    pay_method = models.CharField("Metodo de pago",choices=PAY_METHOD, default='DIGITADO', max_length=100)
    full_payment = models.FloatField('Total abono', null=True, blank=True)
    balance = models.FloatField('Saldo', null=True, blank=True)
    status = models.CharField('Estado admin', choices=STATUS, default='DIGITADO', max_length=100)
    notes = models.TextField("Notas", max_length=500, blank=True)
    added_by = models.ForeignKey(NewUser, on_delete=models.SET_NULL, null=True, verbose_name="Creado por", blank=True)

    class Meta:
        verbose_name = _("Recibos")
        verbose_name_plural = _("Recibos")