# Generated by Django 4.2.6 on 2023-11-01 12:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('medical_manager', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='disease',
            name='treatment',
        ),
        migrations.RemoveField(
            model_name='surgery',
            name='treatment',
        ),
        migrations.AddField(
            model_name='treatment',
            name='disease',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='medical_manager.disease', verbose_name='Enfermedad'),
        ),
        migrations.AddField(
            model_name='treatment',
            name='surgery',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='medical_manager.surgery', verbose_name='Cirugía'),
        ),
    ]
