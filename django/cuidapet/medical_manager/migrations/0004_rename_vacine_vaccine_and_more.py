# Generated by Django 4.2.6 on 2023-11-21 12:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medical_manager', '0003_alter_disease_options_alter_surgery_options_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Vacine',
            new_name='Vaccine',
        ),
        migrations.RenameField(
            model_name='vaccine',
            old_name='vacine_type',
            new_name='vaccine_type',
        ),
    ]