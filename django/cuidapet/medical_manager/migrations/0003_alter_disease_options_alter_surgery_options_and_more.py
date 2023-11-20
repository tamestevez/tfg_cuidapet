# Generated by Django 4.2.6 on 2023-11-20 16:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medical_manager', '0002_remove_disease_treatment_remove_surgery_treatment_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='disease',
            options={'verbose_name': 'Enfermedad', 'verbose_name_plural': 'Enfermedades'},
        ),
        migrations.AlterModelOptions(
            name='surgery',
            options={'verbose_name': 'Cirugía', 'verbose_name_plural': 'Cirugías'},
        ),
        migrations.AlterModelOptions(
            name='treatment',
            options={'verbose_name': 'Tratamiento', 'verbose_name_plural': 'Tratamientos'},
        ),
        migrations.AlterModelOptions(
            name='vacine',
            options={'verbose_name': 'Vacuna', 'verbose_name_plural': 'Vacunas'},
        ),
        migrations.RemoveField(
            model_name='treatment',
            name='disease',
        ),
        migrations.RemoveField(
            model_name='treatment',
            name='surgery',
        ),
    ]