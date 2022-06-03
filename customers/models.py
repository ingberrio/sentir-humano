from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class Customer(AbstractBaseUser):
    
    password = models.CharField("Password", max_length=255)
    first_name = models.CharField("First name", max_length=255)
    last_name = models.CharField("Last name", max_length=255)
    person_id = models.CharField("Cedula", max_length=20, default=' ')
    asesor_id = models.CharField("Asesor encargado", max_length=20, default=' ')
    email = models.EmailField()
    age = models.CharField("Edad", max_length=3, default=' ')
    city = models.CharField("Ciudad", max_length=20, default=' ')
    neigbord = models.CharField("Barrio", max_length=20, default=' ')
    phone = models.CharField(max_length=20)
    address =  models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    createdAt = models.DateTimeField("Created At", auto_now_add=True)
    is_active = models.BooleanField("Activo", default=False)
    
    USERNAME_FIELD = 'email'
    
    def __str__(self):
        return self.first_name