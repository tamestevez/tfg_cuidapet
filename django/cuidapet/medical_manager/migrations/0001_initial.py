# Generated by Django 4.2.6 on 2023-11-01 11:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pet_manager', '0006_animal_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='MedicalHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('allergy', models.CharField(blank=True, max_length=255, null=True, verbose_name='Alergias')),
                ('animal', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pet_manager.animal', verbose_name='Aminal')),
            ],
            options={
                'verbose_name': 'Historial Médico',
                'verbose_name_plural': 'Historiales médicos',
            },
        ),
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manufacturer', models.CharField(max_length=11, verbose_name='Fabricante')),
                ('name', models.CharField(max_length=25, verbose_name='Nombre')),
                ('batch_number', models.CharField(max_length=7, verbose_name='Número de lote')),
                ('expiration_date', models.DateField(verbose_name='Fecha de caducidad')),
                ('start_date', models.DateField(verbose_name='Fecha de inicio')),
                ('ending_date', models.DateField(verbose_name='Fecha de fin')),
                ('medical_history', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medical_manager.medicalhistory')),
                ('veterinary_clinic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Clínica veterinaria')),
            ],
        ),
        migrations.CreateModel(
            name='Treatment',
            fields=[
                ('medicine_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='medical_manager.medicine')),
                ('treatment_type', models.CharField(max_length=25, verbose_name='Tipo de tratamiento')),
                ('chronic', models.BooleanField(default=False, verbose_name='Crónico')),
            ],
            bases=('medical_manager.medicine',),
        ),
        migrations.CreateModel(
            name='Vacine',
            fields=[
                ('medicine_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='medical_manager.medicine')),
                ('vacine_type', models.CharField(max_length=25, verbose_name='Tipo de vacuna')),
                ('vaccination_date', models.DateField(verbose_name='Fecha de vacunación')),
            ],
            bases=('medical_manager.medicine',),
        ),
        migrations.CreateModel(
            name='Surgery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surgery_type', models.CharField(max_length=25, verbose_name='Tipo de cirugía')),
                ('description', models.CharField(max_length=1024, verbose_name='Descripción')),
                ('realization_date', models.DateField(verbose_name='Fecha de realización')),
                ('medical_history', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medical_manager.medicalhistory')),
                ('veterinary_clinic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Clínica veterinaria')),
                ('treatment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medical_manager.treatment', verbose_name='Tratamiento')),
            ],
        ),
        migrations.CreateModel(
            name='Disease',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre')),
                ('description', models.CharField(max_length=255, verbose_name='Descripción')),
                ('medical_history', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medical_manager.medicalhistory')),
                ('veterinary_clinic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Clínica veterinaria')),
                ('treatment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medical_manager.treatment', verbose_name='Tratamiento')),
            ],
        ),
    ]
