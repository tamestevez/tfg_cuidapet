from cuidapet.constants import NATIONALITY
from django.db import models


class InsurancePolice(models.Model):
    code = models.CharField(max_length=15, verbose_name="Número de póliza")
    company_name = models.CharField(max_length=50, verbose_name="Compañía")
    national_helpline = models.CharField(
        max_length=25, verbose_name="Teléfono nacional"
    )
    helpline_abroad = models.CharField(
        max_length=25, verbose_name="Teléfono internacional"
    )
    nationality = models.CharField(
        max_length=2,
        choices=NATIONALITY,
        default="SPAIN",
        verbose_name="Nacionalidad",
    )
    start_date = models.DateTimeField(verbose_name="Fecha de inicio")
    renovation_date = models.DateTimeField(verbose_name="Fecha de renovación")

    def __str__(self):
        return f"{self.company_name} {self.code}"

    class Meta:
        verbose_name = "Poliza de seguro"
        verbose_name_plural = "Polizas de seguros"
