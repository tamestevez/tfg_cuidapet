# Generated by Django 4.2.6 on 2023-11-01 10:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pet_manager', '0003_animal_owner_passport_marking_animal_animal_marking_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='animal',
            name='animal_marking',
        ),
        migrations.RemoveField(
            model_name='animal',
            name='passport',
        ),
        migrations.AddField(
            model_name='marking',
            name='animal',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pet_manager.animal', verbose_name='Animal'),
        ),
        migrations.AddField(
            model_name='passport',
            name='animal',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pet_manager.animal', verbose_name='Animal'),
        ),
    ]