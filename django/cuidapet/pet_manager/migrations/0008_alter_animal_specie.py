# Generated by Django 4.2.6 on 2023-11-20 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pet_manager', '0007_alter_deathrecord_options_alter_marking_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='specie',
            field=models.CharField(choices=[('Perro', (('PASTOR ALEMAN', 'Pastor Alemán'), ('PITWEILER', 'Pitweiler'))), ('Gato', (('HABANA', 'Habana'), ('ELFO', 'Elfo'))), ('Exóticos', (('CONEJO', 'Conejo'), ('AVES', 'Aves')))], max_length=25, verbose_name='Especie'),
        ),
    ]
