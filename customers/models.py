from django.conf import settings
from datetime import datetime
from django.db import models
from memberships.models import Membership
from suppliers.models import Service
from users.models import NewUser
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser
from django.utils.translation import gettext_lazy as _
import re
from simple_history.models import HistoricalRecords

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

CITY =[
    ('ARMENIA', 'ARMENIA'),
    ('CARTAGO', 'CARTAGO'),
    ('QUIMBAYA', 'QUIMBAYA'),
    ('PEREIRA', 'PEREIRA')
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
    value = models.DecimalField("Valor a pagar =", blank=True, max_digits=10, decimal_places = 0, default='0')
    password = models.CharField("Password", max_length=255, default='pbkdf2_sha256$320000$iNI4Mj0nXAjmeRiNnWwZsG$M5fBt/nVaKFdXO35PW+S/paCXgaOcdFZsI6TpAOtx84=')
    address_to_pay =  models.CharField("Direccion para cobrar", blank=True, null=True, max_length=255)
    payment_descount = models.DecimalField('Descuento', blank=True, max_digits=10, decimal_places = 0, help_text='Solo numeros', default=0)
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
    age = models.PositiveSmallIntegerField('Edad', null=True, blank=True,)
    city = models.CharField("Ciudad", choices=CITY, blank=True, max_length=20, default=' ')
    city_pay = models.CharField("Ciudad cobro", choices=CITY, blank=True, max_length=20, default=' ')
    neigbord = models.CharField("Barrio", blank=True, max_length=20, default=' ')
    phone = models.CharField("Telefono", max_length=20)
    phone_contact = models.CharField("Telefono Opcional", blank=True, max_length=20)
    address =  models.CharField("Dirección", blank=True, null=True, max_length=255)
    creator_by = models.ForeignKey(NewUser, related_name='created_by', null=True, blank=True,  on_delete=models.SET_NULL, verbose_name='Creado por')
    description = models.TextField("Notas", blank=True, null=True)
    createdAt = models.DateTimeField("Inicio Cobro",blank=True, null=True)
    endsAt = models.DateTimeField('Finalizacion', blank=True, null=True)
    is_active = models.BooleanField("Activo", default=False)
    is_main = models.BooleanField("Titular", default=False)
    status_membership = models.CharField('Estado', choices=STATUS_MEMBERSHIP, default='DIGITADO', max_length=100)
    gener = models.CharField('Genero', choices=GENER, blank=True, default= ' ', max_length=100)
    history = HistoricalRecords()
    class Meta:
        verbose_name = _("Clientes")
        verbose_name_plural = _("Clientes")
    
    USERNAME_FIELD = 'email'

    
    # Method that subtraction to show in field value
    
    def save(self, *args, **kwargs):
       
            # Save the memmership value in value field
            mem_int = self.membership_id
            mem_int = re.findall('[0-9]+', str(mem_int))
            if mem_int:
                self.value = int(mem_int.pop()) - self.payment_descount
            else:
                self.value = 0
            
            if self.status_membership == 'INCONVENIENTE':
                 self.status_membership = 'INCONVENIENTE'
                 self.is_active = False
            elif self.value > 0:
                 self.status_membership = 'COBRO'
                 self.is_active = True
            else:
                self.status_membership = 'PAGO'
                self.is_active = True
            
            super().save(*args, **kwargs)
            
             

    def __str__(self):
        titular = self.is_main

        if titular == True:
            titular = 'Titular'
        else:
            titular = 'Afliado'
        cadena = titular+" "+self.person_id+" - "+self.first_name+" - $"+str(self.value)
        return cadena

class Appointment(models.Model):
    
    APPOIMENT_CHOICES = [
        ('AFILIACION', 'AFILIACION'),
        ('CITA', 'CITA'),
        ('INFORMACION', 'INFORMACION'),
        ('OTROS', 'OTROS')
    ]
    start_date = models.DateTimeField("Inicio solicitud", default=timezone.now)
    type_appointment = models.CharField("Tipo de cita", max_length=255, choices=APPOIMENT_CHOICES, default='CITA')
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL, verbose_name='Cliente')
    service = models.ForeignKey(Service, null=True, on_delete=models.SET_NULL, verbose_name='Especialidad')
    end_date = models.DateTimeField("Fecha cita", null=True, blank=True)
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, verbose_name="Creado por", blank=True)
    about = models.TextField("Observaciones", max_length=500, blank=True)
    is_confirm = models.BooleanField("Confirmada", default=False)
    is_cancel = models.BooleanField("Cancelada", default=False)
    history = HistoricalRecords()
    
    class Meta:
        verbose_name = _("Citas")
        verbose_name_plural = _("Citas")
    
    def __str__(self):
        return self.type_appointment

class Invoice(models.Model):
    customer = models.ForeignKey(Customer, to_field='id', null=True, on_delete=models.SET_NULL, verbose_name='Cliente')
    contribution_date = models.DateTimeField("Fecha de aporte", default=timezone.now)
    pay_method = models.CharField("Metodo de pago",choices=PAY_METHOD, default='DIGITADO', max_length=100)
    buffer_full_payment = models.DecimalField('Ultimo abono', blank=True, max_digits=10, decimal_places = 0, default=0)
    full_payment = models.DecimalField('Total abono', blank=True, max_digits=10, decimal_places = 0, help_text='Solo numeros', default=0)
    balance = models.DecimalField('Saldo', blank=True, max_digits=10, decimal_places = 0, default=0)
    status = models.CharField('Estado admin', choices=STATUS, default='DIGITADO', max_length=100)
    notes = models.TextField("Notas", max_length=500, blank=True)
    added_by = models.ForeignKey(NewUser, on_delete=models.SET_NULL, null=True, verbose_name="Creado por", blank=True)
    history = HistoricalRecords()

    # Method that subtraction
    def save(self, *args, **kwargs):
        if self.balance == 0:
            self.buffer_full_payment = self.full_payment
            self.balance =int(self.customer.value - self.full_payment)
            self.full_payment = self.full_payment - self.full_payment
        else:
           self.balance = int(self.balance - self.full_payment)
           self.buffer_full_payment = self.full_payment
           self.full_payment = self.full_payment - self.full_payment
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = _("Recibos")
        verbose_name_plural = _("Recibos")

    def __str__(self):
        return str(self.customer)
