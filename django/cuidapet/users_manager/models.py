from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from cuidapet.constants import ROLE

# Create your models here.

class UserManager(BaseUserManager):
    use_in_migrations=True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("El campo email es necesario y obligatorio")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_staff", True)
        return self._create_user(email, password, **extra_fields)
    

class BaseUser(AbstractUser):
    username=None
    first_name=None
    last_login=None
    email=models.EmailField(unique=True)
    opt_generator_code=models.CharField(max_length=50, blank=True, null=True)
    token_password=models.CharField(max_length=255, blank=True, null=True)
    name=models.CharField(blank=True, null=True, verbose_name="Nombre",)
    surnames=models.CharField( blank=True, null=True, verbose_name="Apellidos",)
    phone_number=models.CharField(max_length=15, verbose_name="Teléfono")
    address=models.CharField(max_length=50, null=True, blank=True, verbose_name="Dirección")
    town=models.CharField(max_length=25, blank=True, null=True, verbose_name="Ciudad")
    role=models.CharField(max_length=4, choices=ROLE, default="ADMI", verbose_name="Permisos")


    USERNAME_FIELD="email"
    REQUIRED_FIELDS=[]
    objects=UserManager()
    
    def __str__(self):
        return f"{self.role} {self.email}"
    
    class Meta:
        verbose_name="Usuario"
        verbose_name_plural="Usuarios"
    



    
