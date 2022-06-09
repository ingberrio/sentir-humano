from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from memberships.models import Membership
from suppliers.models import Supplier
from users.models import NewUser
from django.utils import timezone
from django.conf import settings

class Customer(AbstractBaseUser, models.Model):
    membership_id = models.ForeignKey(Membership, null=True, on_delete=models.SET_NULL, verbose_name='Membresia')
    password = models.CharField("Password", max_length=255)
    first_name = models.CharField("First name", max_length=255)
    last_name = models.CharField("Last name", max_length=255)
    person_id = models.CharField("Cedula", max_length=20, default=' ')
    asesor_id = models.ForeignKey(NewUser, null=True, blank=True,  on_delete=models.SET_NULL, verbose_name='Asesor encargado', default='2')
    email = models.EmailField(blank=True)
    age = models.PositiveIntegerField("edad", blank=True)
    city = models.CharField("Ciudad", blank=True, max_length=20, default=' ')
    neigbord = models.CharField("Barrio", blank=True, max_length=20, default=' ')
    phone = models.CharField("Telefono", blank=True, max_length=20)
    address =  models.TextField("Dirección", blank=True, null=True)
    description = models.TextField("Notas", blank=True, null=True)
    createdAt = models.DateTimeField("Created At", auto_now_add=True)
    is_active = models.BooleanField("Activo", default=False)
    
    USERNAME_FIELD = 'email'
    
    def __str__(self):
        return self.person_id

class Appointment(models.Model):
    
    APPOIMENT_CHOICES = [
        ('1', 'Tipo 1'),
        ('2', 'Tipo 2'),
        ('3', 'Tipo 3'),
    ]

    type_appointment = models.CharField("Tipo de cita", max_length=255, choices=APPOIMENT_CHOICES)
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL, verbose_name='Cliente')
    affiliate = models.CharField("Afiliado", max_length=255, blank=True)
    supplier = models.ForeignKey(Supplier, null=True, on_delete=models.SET_NULL, verbose_name='Especialidad')
    start_date = models.DateTimeField("Inicio solicitud", default=timezone.now)
    end_date = models.DateTimeField("Fecha finalizacion", null=True, blank=True)
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, verbose_name="Creado por")
    about = models.TextField("Observaciones", max_length=500, blank=True)
    is_confirm = models.BooleanField("Confirmada", default=False)
    is_cancel = models.BooleanField("Cancelada", default=False)

    # Automatically set to current user to field Author when saved

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            # Only set added_by during the first save.
            obj.added_by = request.user
        super().save_model(request, obj, form, change)

    def __str__(self):
        return self.type_appointment