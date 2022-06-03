from turtle import title
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class CustomAccountManager(BaseUserManager):

    def create_superuser(self, email, username, first_name, password, **other_fields):
    
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser deberia ser asignado is_staf=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser deberia ser asignado is_superuser=True.')
            
        return self.create_user(email, username, first_name, password, **other_fields)

    def create_user(self, email, username, first_name, password, **other_fields):
        
        if not email:
            raise ValueError(_('Debes iniciar con un email'))
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, first_name=first_name, 
                          **other_fields)
        user.set_password(password)
        user.save()
        return user

class NewUser(AbstractBaseUser, PermissionsMixin):
    
    email = models.EmailField(_('Email'), unique=True)
    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150, unique=True)
    last_name = models.CharField(max_length=150, unique=True)
    phone = models.CharField(_('Telefono'),max_length=150, unique=True, default=' ',blank=True)
    address = models.CharField(_('Direccion'),max_length=150, unique=True, default=' ',blank=True)
    neighborhood = models.CharField(_('Barrio'),max_length=150, unique=True, default=' ', blank=True)
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(null=True, blank=True)
    about = models.TextField(_('Observaciones'), max_length=500, blank=True)
    real_id = models.CharField(_('Cedula'),max_length=20, unique=True)
    is_staff = models.BooleanField(_('Empleado'),default=False)
    is_active = models.BooleanField(_('Activo'),default=False)
    
     
    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'password']

    def __str__(self):
        return self.username