# Generated by Django 4.2.6 on 2023-10-31 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users_manager', '0002_alter_baseuser_options_baseuser_address_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='baseuser',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='baseuser',
            name='last_login',
        ),
        migrations.AddField(
            model_name='baseuser',
            name='name',
            field=models.CharField(blank=True, null=True, verbose_name='Nombre'),
        ),
        migrations.AddField(
            model_name='baseuser',
            name='surnames',
            field=models.CharField(blank=True, null=True, verbose_name='Apellidos'),
        ),
        migrations.AlterField(
            model_name='baseuser',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='last name'),
        ),
        migrations.AlterField(
            model_name='baseuser',
            name='phone_number',
            field=models.CharField(max_length=15, verbose_name='Teléfono'),
        ),
        migrations.AlterField(
            model_name='baseuser',
            name='role',
            field=models.CharField(choices=[('PROP', 'PROPIETARIO'), ('PROT', 'PROTECTORA'), ('ADMI', 'ADMINISTRADOR'), ('CLIN', 'CLINICA')], default='ADMI', max_length=4, verbose_name='Permisos'),
        ),
    ]
