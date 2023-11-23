# Generated by Django 4.2.6 on 2023-11-23 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users_manager', '0004_alter_baseuser_town'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baseuser',
            name='town',
            field=models.CharField(blank=True, choices=[('04', 'Almería'), ('11', 'Cádiz'), ('14', 'Córdoba'), ('18', 'Granada'), ('21', 'Huelva'), ('23', 'Jaén'), ('29', 'Málaga'), ('41', 'Sevilla'), ('22', 'Huesca'), ('44', 'Teruel'), ('50', 'Zaragoza'), ('33', 'Asturias'), ('07', 'Illes Balears'), ('35', 'Las Palmas'), ('38', 'Santa Cruz de Tenerife'), ('39', 'Cantabria'), ('05', 'Ávila'), ('09', 'Burgos'), ('24', 'León'), ('34', 'Palencia'), ('37', 'Salamanca'), ('40', 'Segovia'), ('42', 'Soria'), ('47', 'Valladolid'), ('49', 'Zamora'), ('02', 'Albacete'), ('13', 'Ciudad Real'), ('16', 'Cuenca'), ('19', 'Guadalajara'), ('45', 'Toledo'), ('08', 'Barcelona'), ('17', 'Girona'), ('25', 'Lleida'), ('43', 'Tarragona'), ('03', 'Alacant'), ('12', 'Castelló'), ('46', 'València'), ('06', 'Badajoz'), ('10', 'Cáceres'), ('15', 'A Coruña'), ('27', 'Lugo'), ('32', 'Ourense'), ('36', 'Pontevedra'), ('28', 'Madrid'), ('30', 'Murcia'), ('31', 'Navarra'), ('01', 'Araba'), ('48', 'Bizkaia'), ('20', 'Gipuzcoa'), ('26', 'La Rioja'), ('51', 'Ceuta'), ('52', 'Melilla')], max_length=2, null=True, verbose_name='Ciudad'),
        ),
    ]