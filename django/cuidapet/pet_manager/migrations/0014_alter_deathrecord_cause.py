# Generated by Django 4.2.6 on 2023-11-23 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pet_manager", "0013_alter_marking_marking_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="deathrecord",
            name="cause",
            field=models.CharField(
                blank=True,
                choices=[
                    ("00", "Cáncer"),
                    ("01", "Diabetes"),
                    ("02", "Diarrea Neonatal"),
                    ("03", "Enfermedades Cardíacas"),
                    ("04", "Enfermedades Gastrointestinales"),
                    ("05", "Enfermedades Infecciosas"),
                    ("06", "Enfermedades Metabólicas"),
                    ("07", "Enfermedades Renales"),
                    ("08", "Enfermedades Respiratorias"),
                    ("09", "Envenenamiento"),
                    ("10", "Insuficiencia Renal"),
                    ("11", "Infecciones Clostridiales"),
                    ("12", "Infecciones Reproductivas"),
                    ("13", "Infecciones Virales"),
                    ("14", "Parásitos Internos y Externos"),
                    ("15", "Problemas de Alimentación"),
                    ("16", "Problemas de Parto"),
                    ("17", "Problemas de Pie y Pezuña"),
                    ("18", "Problemas Metabólicos"),
                    ("19", "Traumatismos"),
                ],
                max_length=50,
                null=True,
                verbose_name="Causa",
            ),
        ),
    ]
