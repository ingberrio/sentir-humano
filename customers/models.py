from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from memberships.models import Membership
from users.models import NewUser

class Customer(AbstractBaseUser, models.Model):
    membership_id = models.ForeignKey(Membership, null=True, on_delete=models.SET_NULL, verbose_name='Membresia')
    password = models.CharField("Password", max_length=255)
    first_name = models.CharField("First name", max_length=255)
    last_name = models.CharField("Last name", max_length=255)
    person_id = models.CharField("Cedula", max_length=20, default=' ')
    asesor_id = models.ForeignKey(NewUser, null=True, on_delete=models.SET_NULL, verbose_name='Asesor encargado', default='2')
    email = models.EmailField()
    age = models.CharField("Edad", max_length=3, default=' ')
    city = models.CharField("Ciudad", max_length=20, default=' ')
    neigbord = models.CharField("Barrio", max_length=20, default=' ')
    phone = models.CharField("Telefono", max_length=20)
    address =  models.TextField("Dirección", blank=True, null=True)
    description = models.TextField("Notas", blank=True, null=True)
    createdAt = models.DateTimeField("Created At", auto_now_add=True)
    is_active = models.BooleanField("Activo", default=False)
    
    USERNAME_FIELD = 'email'
    
    def __str__(self):
        return self.first_name