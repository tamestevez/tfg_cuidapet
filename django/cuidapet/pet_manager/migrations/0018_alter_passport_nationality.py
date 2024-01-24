# Generated by Django 4.2.6 on 2024-01-24 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pet_manager', '0017_alter_passport_nationality'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passport',
            name='nationality',
            field=models.CharField(choices=[('AD', 'Andorra'), ('TF', 'Tierras Australes y Antárticas Francesas'), ('LA', 'Laos'), ('CA', 'Canadá'), ('NG', 'Nigeria'), ('VU', 'Vanuatu'), ('CZ', 'Chequia'), ('MW', 'Malawi'), ('ML', 'Mali'), ('IS', 'Islandia'), ('NO', 'Noruega'), ('VC', 'San Vicente y Granadinas'), ('GP', 'Guadalupe'), ('CL', 'Chile'), ('BM', 'Bermudas'), ('KW', 'Kuwait'), ('DM', 'Dominica'), ('ME', 'Montenegro'), ('VI', 'Islas Vírgenes de los Estados Unidos'), ('CM', 'Camerún'), ('LK', 'Sri Lanka'), ('CN', 'China'), ('BD', 'Bangladesh'), ('SE', 'Suecia'), ('GD', 'Grenada'), ('TR', 'Turquía'), ('GN', 'Guinea'), ('TZ', 'Tanzania'), ('RW', 'Ruanda'), ('SG', 'Singapur'), ('MA', 'Marruecos'), ('BL', 'San Bartolomé'), ('IQ', 'Irak'), ('BN', 'Brunei'), ('IM', 'Isla de Man'), ('KP', 'Corea del Norte'), ('IR', 'Iran'), ('CW', 'Curazao'), ('PY', 'Paraguay'), ('AL', 'Albania'), ('TJ', 'Tayikistán'), ('BO', 'Bolivia'), ('AT', 'Austria'), ('KN', 'San Cristóbal y Nieves'), ('UM', 'Islas Ultramarinas Menores de Estados Unidos'), ('CO', 'Colombia'), ('XK', 'Kosovo'), ('BZ', 'Belice'), ('GW', 'Guinea-Bisáu'), ('MH', 'Islas Marshall'), ('MM', 'Myanmar'), ('PF', 'Polinesia Francesa'), ('BR', 'Brasil'), ('HR', 'Croacia'), ('SO', 'Somalia'), ('AF', 'Afganistán'), ('AI', 'Anguilla'), ('CK', 'Islas Cook'), ('EH', 'Sahara Occidental'), ('NZ', 'Nueva Zelanda'), ('ER', 'Eritrea'), ('KH', 'Camboya'), ('BS', 'Bahamas'), ('BY', 'Bielorrusia'), ('NF', 'Isla de Norfolk'), ('TV', 'Tuvalu'), ('GS', 'Islas Georgias del Sur y Sandwich del Sur'), ('MR', 'Mauritania'), ('NC', 'Nueva Caledonia'), ('BG', 'Bulgaria'), ('MZ', 'Mozambique'), ('NU', 'Niue'), ('EE', 'Estonia'), ('IT', 'Italia'), ('MT', 'Malta'), ('SI', 'Eslovenia'), ('IN', 'India'), ('PE', 'Perú'), ('BI', 'Burundi'), ('LT', 'Lituania'), ('US', 'Estados Unidos'), ('HN', 'Honduras'), ('TO', 'Tonga'), ('SA', 'Arabia Saudí'), ('SR', 'Surinam'), ('QA', 'Catar'), ('SH', 'Santa Elena, Ascensión y Tristán de Acuña'), ('GI', 'Gibraltar'), ('MP', 'Islas Marianas del Norte'), ('MU', 'Mauricio'), ('BB', 'Barbados'), ('RE', 'Reunión'), ('IO', 'Territorio Británico del Océano Índico'), ('SY', 'Siria'), ('EG', 'Egipto'), ('ST', 'Santo Tomé y Príncipe'), ('KI', 'Kiribati'), ('TL', 'Timor Oriental'), ('LS', 'Lesotho'), ('SB', 'Islas Salomón'), ('LY', 'Libia'), ('KR', 'Corea del Sur'), ('LI', 'Liechtenstein'), ('NI', 'Nicaragua'), ('EC', 'Ecuador'), ('MV', 'Maldivas'), ('DZ', 'Argelia'), ('KG', 'Kirguizistán'), ('FI', 'Finlandia'), ('AQ', 'Antártida'), ('KE', 'Kenia'), ('CU', 'Cuba'), ('MS', 'Montserrat'), ('PL', 'Polonia'), ('AX', 'Alandia'), ('ET', 'Etiopía'), ('TG', 'Togo'), ('BA', 'Bosnia y Herzegovina'), ('UY', 'Uruguay'), ('GU', 'Guam'), ('CV', 'Cabo Verde'), ('TD', 'Chad'), ('VA', 'Ciudad del Vaticano'), ('PW', 'Palau'), ('HT', 'Haití'), ('YE', 'Yemen'), ('SZ', 'Suazilandia'), ('ZW', 'Zimbabue'), ('GR', 'Grecia'), ('IL', 'Israel'), ('MF', 'Saint Martin'), ('AG', 'Antigua y Barbuda'), ('CY', 'Chipre'), ('SX', 'Sint Maarten'), ('MC', 'Mónaco'), ('FJ', 'Fiyi'), ('UA', 'Ucrania'), ('MQ', 'Martinica'), ('HK', 'Hong Kong'), ('PT', 'Portugal'), ('BT', 'Bután'), ('NP', 'Nepal'), ('FR', 'Francia'), ('IE', 'Irlanda'), ('AE', 'Emiratos Árabes Unidos'), ('GG', 'Guernsey'), ('LC', 'Santa Lucía'), ('DO', 'República Dominicana'), ('RS', 'Serbia'), ('BW', 'Botswana'), ('CI', 'Costa de Marfil'), ('GH', 'Ghana'), ('KM', 'Comoras'), ('AZ', 'Azerbaiyán'), ('GB', 'Reino Unido'), ('CF', 'República Centroafricana'), ('PS', 'Palestina'), ('BQ', 'Caribe Neerlandés'), ('TW', 'Taiwán'), ('PN', 'Islas Pitcairn'), ('SM', 'San Marino'), ('SJ', 'Islas Svalbard y Jan Mayen'), ('DJ', 'Djibouti'), ('WF', 'Wallis y Futuna'), ('DK', 'Dinamarca'), ('PG', 'Papúa Nueva Guinea'), ('MG', 'Madagascar'), ('BV', 'Isla Bouvet'), ('HU', 'Hungría'), ('TK', 'Islas Tokelau'), ('TT', 'Trinidad y Tobago'), ('GM', 'Gambia'), ('LU', 'Luxemburgo'), ('CC', 'Islas Cocos o Islas Keeling'), ('CG', 'Congo'), ('AR', 'Argentina'), ('CD', 'Congo (Rep. Dem.)'), ('GL', 'Groenlandia'), ('JO', 'Jordania'), ('BE', 'Bélgica'), ('CH', 'Suiza'), ('ID', 'Indonesia'), ('LB', 'Líbano'), ('MY', 'Malasia'), ('KY', 'Islas Caimán'), ('SK', 'República Eslovaca'), ('AM', 'Armenia'), ('CX', 'Isla de Navidad'), ('MN', 'Mongolia'), ('PM', 'San Pedro y Miquelón'), ('JP', 'Japón'), ('ZA', 'Sudáfrica'), ('PH', 'Filipinas'), ('FM', 'Micronesia'), ('DE', 'Alemania'), ('LV', 'Letonia'), ('JM', 'Jamaica'), ('MO', 'Macao'), ('NR', 'Nauru'), ('FO', 'Islas Faroe'), ('GY', 'Guyana'), ('BF', 'Burkina Faso'), ('SD', 'Sudán'), ('RU', 'Rusia'), ('YT', 'Mayotte'), ('AU', 'Australia'), ('LR', 'Liberia'), ('MX', 'México'), ('TN', 'Túnez'), ('AW', 'Aruba'), ('KZ', 'Kazajistán'), ('OM', 'Omán'), ('GF', 'Guayana Francesa'), ('NE', 'Níger'), ('TM', 'Turkmenistán'), ('SL', 'Sierra Leone'), ('WS', 'Samoa'), ('SN', 'Senegal'), ('GE', 'Georgia'), ('NA', 'Namibia'), ('SS', 'Sudán del Sur'), ('TH', 'Tailandia'), ('BH', 'Bahrein'), ('HM', 'Islas Heard y McDonald'), ('FK', 'Islas Malvinas'), ('JE', 'Jersey'), ('VN', 'Vietnam'), ('GT', 'Guatemala'), ('MD', 'Moldavia'), ('MK', 'Macedonia del Norte'), ('UZ', 'Uzbekistán'), ('RO', 'Rumania'), ('UG', 'Uganda'), ('SV', 'El Salvador'), ('ZM', 'Zambia'), ('GA', 'Gabón'), ('GQ', 'Guinea Ecuatorial'), ('ES', 'España'), ('NL', 'Países Bajos'), ('VG', 'Islas Vírgenes del Reino Unido'), ('BJ', 'Benín'), ('PK', 'Pakistán'), ('PA', 'Panamá'), ('TC', 'Islas Turks y Caicos'), ('AO', 'Angola'), ('AS', 'Samoa Americana'), ('VE', 'Venezuela'), ('CR', 'Costa Rica'), ('PR', 'Puerto Rico'), ('SC', 'Seychelles')], default='SPAIN', max_length=2, verbose_name='Nacionalidad'),
        ),
    ]