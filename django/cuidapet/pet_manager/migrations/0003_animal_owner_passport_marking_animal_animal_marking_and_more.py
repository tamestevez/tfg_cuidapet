# Generated by Django 4.2.6 on 2023-11-01 10:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pet_manager', '0002_alter_animal_atttitudes_alter_animal_birth_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Propietario'),
        ),
        migrations.CreateModel(
            name='Passport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=11, unique=True, verbose_name='Código')),
                ('expedition_date', models.DateField(verbose_name='Fecha de expedición')),
                ('nationality', models.CharField(choices=[('AL', 'ALBANIA'), ('ES', 'SPAIN')], default='SPAIN', max_length=2, verbose_name='Nacionalidad')),
                ('veterinary_clinic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Clinica veterinaria')),
            ],
        ),
        migrations.CreateModel(
            name='Marking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=15, unique=True, verbose_name='Código')),
                ('marking_type', models.CharField(max_length=4, verbose_name='Tipo de marca')),
                ('expedition_date', models.DateField(verbose_name='Fecha de colocación')),
                ('location', models.CharField(max_length=50, verbose_name='Localización de la marca')),
                ('veterinary_clinic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Clínica veterinaria')),
            ],
        ),
        migrations.AddField(
            model_name='animal',
            name='animal_marking',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pet_manager.marking', verbose_name='Marcaje'),
        ),
        migrations.AddField(
            model_name='animal',
            name='passport',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pet_manager.passport', verbose_name='Pasaporte'),
        ),
    ]
