# Generated by Django 4.2.6 on 2023-11-20 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pet_manager", "0006_animal_image"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="deathrecord",
            options={"verbose_name": "Registro de defunción"},
        ),
        migrations.AlterModelOptions(
            name="marking",
            options={"verbose_name": "Marca"},
        ),
        migrations.AlterModelOptions(
            name="passport",
            options={"verbose_name": "Pasaporte"},
        ),
        migrations.AlterField(
            model_name="passport",
            name="nationality",
            field=models.CharField(
                choices=[
                    ("AF", "Afganistán"),
                    ("ZA", "Sudáfrica"),
                    ("AL", "Albania"),
                    ("DE", "Alemania"),
                    ("AD", "Andorra"),
                    ("AO", "Angola"),
                    ("AI", "Anguila"),
                    ("AG", "Antigua y Barbuda"),
                    ("AN", "Antillas Holandesas"),
                    ("SA", "Arabia Saudita"),
                    ("DZ", "Argelia"),
                    ("AR", "Argentina"),
                    ("AM", "Armenia"),
                    ("AW", "Aruba"),
                    ("AU", "Australia"),
                    ("AT", "Austria"),
                    ("AZ", "Azerbaiyán"),
                    ("BS", "Bahamas"),
                    ("BD", "Bangladesh"),
                    ("BB", "Barbados"),
                    ("BH", "Baréin"),
                    ("BE", "Bélgica"),
                    ("BZ", "Belice"),
                    ("BJ", "Benín"),
                    ("BM", "Islas Bermudas"),
                    ("BY", "Bielorrusia"),
                    ("BO", "Bolivia"),
                    ("BA", "Bosnia Herzegovina"),
                    ("BW", "Botsuana"),
                    ("BR", "Brasil"),
                    ("BN", "Brunéi"),
                    ("BG", "Bulgaria"),
                    ("BF", "Burkina Faso"),
                    ("BI", "Burundi"),
                    ("BT", "Bután"),
                    ("CV", "Cabo Verde"),
                    ("CM", "Camerún"),
                    ("KH", "Camboya"),
                    ("CA", "Canadá"),
                    ("QA", "Katar"),
                    ("KZ", "Kazajstán"),
                    ("TD", "Chad"),
                    ("CL", "Chile"),
                    ("CN", "China"),
                    ("CY", "Chipre"),
                    ("CO", "Colombia"),
                    ("CG", "Congo"),
                    ("KP", "Corea del Norte"),
                    ("KR", "Corea del Sur"),
                    ("CI", "Costa de Marfil"),
                    ("CR", "Costa Rica"),
                    ("HR", "Croacia"),
                    ("CU", "Cuba"),
                    ("CW", "Curazao"),
                    ("DK", "Dinamarca"),
                    ("DJ", "Yibuti"),
                    ("DM", "Dominica"),
                    ("EG", "Egipto"),
                    ("SV", "El Salvador"),
                    ("AE", "Emiratos Árabes Unidos"),
                    ("EC", "Ecuador"),
                    ("ER", "Eritrea"),
                    ("SK", "Eslovaquia"),
                    ("SI", "Eslovenia"),
                    ("ES", "España"),
                    ("US", "Estados Unidos"),
                    ("EE", "Estonia"),
                    ("ET", "Etiopía"),
                    ("FJ", "Fiyi"),
                    ("PH", "Filipinas"),
                    ("FI", "Finlandia"),
                    ("FR", "Francia"),
                    ("GA", "Gabón"),
                    ("GM", "Gambia"),
                    ("GH", "Gana"),
                    ("GI", "Gibraltar"),
                    ("GD", "Granada"),
                    ("GR", "Grecia"),
                    ("GL", "Groenlandia"),
                    ("GP", "Guadalupe"),
                    ("GU", "Guam"),
                    ("GT", "Guatemala"),
                    ("GY", "Guayana"),
                    ("GF", "Guayana Francesa"),
                    ("GN", "Guinea"),
                    ("GQ", "Guinea Ecuatorial"),
                    ("GW", "Guinea-Bisáu"),
                    ("HT", "Haití"),
                    ("NL", "Países Bajos"),
                    ("HN", "Honduras"),
                    ("HK", "Hong Kong"),
                    ("HU", "Hungría"),
                    ("YE", "Yemen"),
                    ("BV", "Isla Bouvet"),
                    ("UM", "Isla Periférica Menor"),
                    ("NF", "Isla Norfolk"),
                    ("RE", "Isla Reunión"),
                    ("ST", "Isla Santo Tomé y Príncipe"),
                    ("KY", "Islas Caimán"),
                    ("CX", "Islas de Navidad"),
                    ("CC", "Islas de Coco"),
                    ("KM", "Islas Comoras"),
                    ("CK", "Islas Cook"),
                    ("FK", "Islas Malvinas"),
                    ("FO", "Islas Faroe"),
                    ("HM", "Islas Heard & McDonald"),
                    ("MP", "Islas Marianas del Norte"),
                    ("MH", "Islas Marshall"),
                    ("MU", "Islas Mauricio"),
                    ("SB", "Islas Salomón"),
                    ("SJ", "Islas Svalbard y Jan Mayan"),
                    ("TC", "Islas Turcas y Caicos"),
                    ("VI", "Islas Vírgenes de los Estados Unidos"),
                    ("VG", "Islas Vírgenes Británicas"),
                    ("WF", "Islas Wallis y Futuna"),
                    ("IN", "India"),
                    ("ID", "Indonesia"),
                    ("IG", "Inglaterra"),
                    ("IR", "Irán"),
                    ("IQ", "Irak"),
                    ("IE", "Irlanda"),
                    ("IS", "Islandia"),
                    ("IL", "Israel"),
                    ("IT", "Italia"),
                    ("YU", "Yugoslavia"),
                    ("JM", "Jamaica"),
                    ("JP", "Japón"),
                    ("JO", "Jordán"),
                    ("KI", "Kiribati"),
                    ("KW", "Kuwait"),
                    ("LA", "Laos"),
                    ("LS", "Lesoto"),
                    ("LV", "Letonia"),
                    ("LB", "Líbano"),
                    ("LR", "Liberia"),
                    ("LY", "Libia"),
                    ("LI", "Liechtenstein"),
                    ("LT", "Lituania"),
                    ("LU", "Luxemburgo"),
                    ("MK", "Macedonia"),
                    ("MG", "Madagascar"),
                    ("MY", "Malasia"),
                    ("MW", "Malauí"),
                    ("MV", "Maldivas"),
                    ("ML", "Malí"),
                    ("MT", "Malta"),
                    ("MA", "Marruecos"),
                    ("MQ", "Martinica"),
                    ("IM", "Mauricio"),
                    ("MR", "Mauritania"),
                    ("YT", "Mayotte"),
                    ("MX", "México"),
                    ("MM", "Birmania"),
                    ("FM", "Micronesia"),
                    ("MZ", "Mozambique"),
                    ("MD", "Moldavia"),
                    ("MC", "Mónaco"),
                    ("MN", "Mongolia"),
                    ("ME", "Montenegro"),
                    ("MS", "Montserrat"),
                    ("NA", "Namibia"),
                    ("NR", "Nauru"),
                    ("NP", "Nepal"),
                    ("NI", "Nicaragua"),
                    ("NE", "Níger"),
                    ("NG", "Nigeria"),
                    ("NU", "Niue"),
                    ("NO", "Noruega"),
                    ("NC", "Nueva Caledonia"),
                    ("NZ", "Nueva Zelanda"),
                    ("OM", "Omán"),
                    ("PW", "Palaos"),
                    ("PS", "Palestina"),
                    ("PA", "Panamá"),
                    ("PG", "Papúa Nueva Guinea"),
                    ("PK", "Pakistán"),
                    ("PY", "Paraguay"),
                    ("PE", "Perú"),
                    ("PN", "Pitcairn"),
                    ("PF", "Polinesia Francesa"),
                    ("PL", "Polonia"),
                    ("PR", "Puerto Rico"),
                    ("PT", "Portugal"),
                    ("KE", "Kenia"),
                    ("KG", "Kirguistán"),
                    ("GB", "Reino Unido"),
                    ("CF", "República Centroafricana"),
                    ("GE", "Republica de Georgia"),
                    ("CD", "República Democrática del Congo"),
                    ("DO", "República Dominicana"),
                    ("CZ", "República Checa"),
                    ("RO", "Rumania"),
                    ("RW", "Ruanda"),
                    ("RU", "Rusia"),
                    ("EH", "Sahara Occidental"),
                    ("BL", "San Bartolomé"),
                    ("PM", "San Pedro y Miquelón"),
                    ("AS", "Samoa Americana"),
                    ("WS", "Samoa Occidental"),
                    ("SM", "San Marino"),
                    ("SH", "Santa Helena"),
                    ("LC", "Santa Lucía"),
                    ("KN", "San Cristóbal y Nieves"),
                    ("TS", "San Martín"),
                    ("VC", "San Vicente y las Granadinas"),
                    ("YC", "Seychelles"),
                    ("SN", "Senegal"),
                    ("SL", "Sierra Leona"),
                    ("RS", "Serbia"),
                    ("SG", "Singapur"),
                    ("SY", "Siria"),
                    ("SO", "Somalia"),
                    ("LK", "Sri Lanka"),
                    ("SZ", "Suazilandia"),
                    ("SD", "Sudán"),
                    ("SS", "Sudán del Sur"),
                    ("SE", "Suecia"),
                    ("CH", "Suiza"),
                    ("SR", "Surinam"),
                    ("TJ", "Tayikistán"),
                    ("TH", "Tailandia"),
                    ("TW", "Taiwán"),
                    ("TZ", "Tanzania"),
                    ("TL", "Timor Oriental"),
                    ("TG", "Togo"),
                    ("TK", "Tokelau"),
                    ("TO", "Tonga"),
                    ("TT", "Trinidad y Tobago"),
                    ("TN", "Túnez"),
                    ("TM", "Turkmenistán"),
                    ("TC", "Turcas y Caicos"),
                    ("TR", "Turquía"),
                    ("TV", "Tuvalu"),
                    ("UA", "Ucrania"),
                    ("UG", "Uganda"),
                    ("UY", "Uruguay"),
                    ("UZ", "Uzbekistán"),
                    ("VU", "Vanuatu"),
                    ("VE", "Venezuela"),
                    ("VN", "Vietnam"),
                    ("ZM", "Zambia"),
                    ("ZW", "Zimbabue"),
                ],
                default="SPAIN",
                max_length=2,
                verbose_name="Nacionalidad",
            ),
        ),
    ]
