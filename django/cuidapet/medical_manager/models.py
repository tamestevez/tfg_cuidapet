from django.db import models
from multiselectfield import MultiSelectField
from pet_manager.models import Animal
from users_manager.models import BaseUser
from cuidapet.constants import TREATMENT_TYPE, SURGERY_TYPE, VACCINE_TYPE,ALERGY

# Create your models here.

class MedicalHistory(models.Model):
    animal=models.ForeignKey(Animal, blank=True, null=True, on_delete=models.CASCADE, verbose_name="Aminal")
    allergy=MultiSelectField(max_length=25, choices=ALERGY, blank=True, null=True, verbose_name="Alergias")
    allergy_description=models.CharField(max_length=255, null=True, blank=True, verbose_name="Descripción de alergias")

    def __str__(self) -> str:
        return self.animal.name
    class Meta:
        verbose_name="Historial Médico"
        verbose_name_plural="Historiales médicos"

class Disease(models.Model):
    name=models.CharField(max_length=50, verbose_name="Nombre")
    description=models.CharField(max_length=255, verbose_name="Descripción")
    veterinary_clinic=models.ForeignKey(BaseUser, on_delete=models.CASCADE, verbose_name="Clínica veterinaria")
    medical_history=models.ForeignKey(MedicalHistory, on_delete=models.CASCADE)

    class Meta:
        verbose_name="Enfermedad"
        verbose_name_plural="Enfermedades"

class Surgery(models.Model):
    surgery_type=models.CharField(max_length=2, choices=SURGERY_TYPE, default="00", verbose_name="Tipo de cirugía")
    description=models.CharField(max_length=1024, verbose_name="Descripción")
    veterinary_clinic=models.ForeignKey(BaseUser, on_delete=models.CASCADE, verbose_name="Clínica veterinaria")
    realization_date=models.DateField(verbose_name="Fecha de realización")
    medical_history=models.ForeignKey(MedicalHistory, on_delete=models.CASCADE)

    class Meta:
        verbose_name="Cirugía"
        verbose_name_plural="Cirugías"

class Medicine(models.Model):
    manufacturer=models.CharField(max_length=11, verbose_name="Fabricante")
    name=models.CharField(max_length=25, verbose_name="Nombre")
    batch_number=models.CharField(max_length=7, verbose_name="Número de lote")
    expiration_date=models.DateField(verbose_name="Fecha de caducidad")
    start_date=models.DateField(verbose_name="Fecha de inicio")
    ending_date=models.DateField(verbose_name="Fecha de fin")
    veterinary_clinic=models.ForeignKey(BaseUser, on_delete=models.CASCADE, verbose_name="Clínica veterinaria")
    medical_history=models.ForeignKey(MedicalHistory, on_delete=models.CASCADE)

class Vaccine(Medicine):
    vaccine_type=models.CharField(max_length=2, choices=VACCINE_TYPE, default="00", verbose_name="Tipo de vacuna")
    vaccination_date=models.DateField(verbose_name="Fecha de vacunación")

    class Meta:
        verbose_name="Vacuna"
        verbose_name_plural="Vacunas"

class Treatment(Medicine):
    treatment_type=models.CharField(max_length=2, choices=TREATMENT_TYPE, default="00", verbose_name="Tipo de tratamiento")
    chronic=models.BooleanField(default=False, verbose_name="Crónico")

    class Meta:
        verbose_name="Tratamiento"
        verbose_name_plural="Tratamientos"

    