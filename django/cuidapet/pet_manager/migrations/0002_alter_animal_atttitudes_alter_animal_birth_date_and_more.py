# Generated by Django 4.2.6 on 2023-10-31 09:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('insurance_manager', '0001_initial'),
        ('pet_manager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='atttitudes',
            field=models.CharField(max_length=15, verbose_name='Actitudes'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='birth_date',
            field=models.DateField(verbose_name='Fecha de nacimiento'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='breed',
            field=models.CharField(max_length=25, verbose_name='Raza'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='color',
            field=models.CharField(max_length=15, verbose_name='Color'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='insurance_police',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='insurance_manager.insurancepolice', verbose_name='Poliza de seguro'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='notable_characteristics',
            field=models.CharField(max_length=255, verbose_name='Caracteristicas'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='ppp',
            field=models.BooleanField(default=False, verbose_name='PPP'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='sex',
            field=models.CharField(choices=[('F', 'FEMIA'), ('M', 'MACHO')], default='F', max_length=1, verbose_name='Sexo'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='specie',
            field=models.CharField(max_length=25, verbose_name='Especie'),
        ),
    ]
