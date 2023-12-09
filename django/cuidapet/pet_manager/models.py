from cuidapet.constants import (
    ATTITUDES,
    COLOR,
    DEATH_CAUSE,
    MARKING_TYPE,
    NATIONALITY,
    ROLE,
    SEX,
    SPECIE,
)
from django.db import models
from insurance_manager.models import InsurancePolice
from multiselectfield import MultiSelectField
from users_manager.models import BaseUser

# Create your models here.


class Animal(models.Model):
    name = models.CharField(
        max_length=50, blank=False, null=False, verbose_name="Nombre"
    )
    specie = models.CharField(
        max_length=50, choices=SPECIE, verbose_name="Especie"
    )
    sex = models.CharField(
        max_length=1, choices=SEX, default="F", verbose_name="Sexo"
    )
    birth_date = models.DateField(verbose_name="Fecha de nacimiento")
    color = MultiSelectField(
        max_length=50, choices=COLOR, verbose_name="Color"
    )
    notable_characteristics = models.CharField(
        max_length=255, verbose_name="Caracteristicas"
    )
    owner = models.ForeignKey(
        BaseUser,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        verbose_name="Propietario",
    )
    ppp = models.BooleanField(default=False, verbose_name="PPP")
    attitudes = MultiSelectField(
        max_length=15,
        choices=ATTITUDES,
        blank=True,
        null=True,
        max_choices=2,
        verbose_name="Actitudes",
    )
    insurance_police = models.ForeignKey(
        InsurancePolice,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        verbose_name="Poliza de seguro",
    )
    image = models.ImageField(null=True, verbose_name="Imagen de perfil")

    def __str__(self):
        return self.name

    @property
    def adopted(self):
        if self.owner.role == ROLE["PROP"]:
            return True
        elif self.owner.role == ROLE.PROT:
            return False

    class Meta:
        verbose_name = "Mascota"
        verbose_name_plural = "Mascotas"


class Marking(models.Model):
    code = models.CharField(
        max_length=15,
        unique=True,
        null=False,
        blank=False,
        verbose_name="Código",
    )
    marking_type = models.CharField(
        max_length=2,
        choices=MARKING_TYPE,
        default="05",
        verbose_name="Tipo de marca",
    )
    expedition_date = models.DateField(verbose_name="Fecha de colocación")
    location = models.CharField(
        max_length=50, verbose_name="Localización de la marca"
    )
    veterinary_clinic = models.ForeignKey(
        BaseUser, on_delete=models.CASCADE, verbose_name="Clínica veterinaria"
    )
    animal = models.ForeignKey(
        Animal, on_delete=models.CASCADE, null=True, verbose_name="Animal"
    )

    class Meta:
        verbose_name = "Marca"


class Passport(models.Model):
    code = models.CharField(
        max_length=11,
        unique=True,
        blank=False,
        null=False,
        verbose_name="Código",
    )
    expedition_date = models.DateField(verbose_name="Fecha de expedición")
    veterinary_clinic = models.ForeignKey(
        BaseUser, on_delete=models.CASCADE, verbose_name="Clinica veterinaria"
    )
    nationality = models.CharField(
        max_length=2,
        choices=NATIONALITY,
        default="SPAIN",
        verbose_name="Nacionalidad",
    )
    animal = models.ForeignKey(
        Animal, on_delete=models.CASCADE, null=True, verbose_name="Animal"
    )

    class Meta:
        verbose_name = "Pasaporte"


class DeathRecord(models.Model):
    death_date = models.DateField(verbose_name="Fecha de fallecimiento")
    veterinary_clinic = models.ForeignKey(
        BaseUser, on_delete=models.CASCADE, verbose_name="Clinica Veterinaria"
    )
    cause = models.CharField(
        max_length=50,
        choices=DEATH_CAUSE,
        null=True,
        blank=True,
        verbose_name="Causa",
    )
    animal = models.ForeignKey(
        Animal, on_delete=models.CASCADE, null=True, verbose_name="Animal"
    )

    class Meta:
        verbose_name = "Registro de defunción"
