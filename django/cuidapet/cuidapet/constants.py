from .utils import get_constants

NATIONALITY = [
    (country["cca2"], country["translations"]["spa"]["common"])
    for country in get_constants("nationalities")
]

SEX = [
    ("F", "FEMIA"),
    ("M", "MACHO"),
]

ROLE = [
    ("PROP", "PROPIETARIO"),
    ("PROT", "PROTECTORA"),
    ("ADMI", "ADMINISTRADOR"),
    ("CLIN", "CLINICA"),
]


SPECIE = (
    (
        "Perro",
        [(dog["name"], dog["name"]) for dog in get_constants("dogs")]
        if get_constants("dogs")
        else [("Perro", "Perro")],
    ),
    (
        "Gato",
        [(dog["name"], dog["name"]) for dog in get_constants("cats")]
        if get_constants("cats")
        else [("Perro", "Perro")],
    ),
    (
        "Exótico",
        [
            ("ARAÑA", "Araña"),
            ("CHINCHILLA", "Chinchilla"),
            ("COBAYA", "Cobaya"),
            ("ERIZO", "Erizo"),
            ("HURON", "Hurón"),
            ("PEZ", "Pez"),
            ("REPTIL", "Reptil"),
        ],
    ),
    (
        "Otros",
        [
            ("AVE", "Ave"),
            ("BOVINO", "Bovino"),
            ("CABALLO", "Caballo"),
            ("CERDO", "Cerdo"),
            ("CONEJO", "Conejo"),
            ("OTRO", "Otro"),
        ],
    ),
)

TOWN = [
    (town["codigo"], town["provincia"])
    for town in get_constants("towns")["results"]
]

MARKING_TYPE = [
    ("00", "Anilla"),
    ("01", "Branding"),
    ("02", "Collar de seguimiento"),
    ("03", "Etiqueta"),
    ("04", "Marca"),
    ("05", "Microchip"),
    ("06", "Tatuaje"),
    ("07", "Tinta"),
]

DEATH_CAUSE = [
    ("00", "Cáncer"),
    ("01", "Diabetes"),
    ("02", "Diarrea Neonatal"),
    ("03", "Enfermedades Cardíacas"),
    ("04", "Enfermedades Gastrointestinales"),
    ("05", "Enfermedades Infecciosas"),
    ("06", "Enfermedades Metabólicas"),
    ("07", "Enfermedades Renales"),
    ("08", "Enfermedades Respiratorias"),
    ("09", "Envenenamiento"),
    ("10", "Insuficiencia Renal"),
    ("11", "Infecciones Clostridiales"),
    ("12", "Infecciones Reproductivas"),
    ("13", "Infecciones Virales"),
    ("14", "Parásitos Internos y Externos"),
    ("15", "Problemas de Alimentación"),
    ("16", "Problemas de Parto"),
    ("17", "Problemas de Pie y Pezuña"),
    ("18", "Problemas Metabólicos"),
    ("19", "Traumatismos"),
]

TREATMENT_TYPE = [
    ("00", "Desparasitación"),
    ("01", "Fisioterapia"),
    ("02", "Inyecciones"),
    ("03", "Medicamentos Orales"),
    ("04", "Quimioterapia"),
    ("05", "Radioterapia"),
    ("06", "Terapia Conductual"),
    ("07", "Terapia de Fluidos"),
    ("08", "Terapia de Oxígeno"),
    ("09", "Terapia Hormonal"),
    ("10", "Terapia Laser"),
    ("11", "Terapia Nutricional"),
    ("12", "Tratamientos Dentales"),
    ("13", "Tratamientos Homeopáticos"),
    ("14", "Tratamientos Tópicos"),
]

SURGERY_TYPE = [
    ("00", "Cirugía Cardiovascular"),
    ("01", "Cirugía de Emergencia"),
    ("02", "Cirugía Dental"),
    ("03", "Cirugía Gastrointestinal"),
    ("04", "Cirugía Neurológica"),
    ("05", "Cirugía Oftalmológica"),
    ("06", "Cirugía de Oído"),
    ("07", "Cirugía Oncológica"),
    ("08", "Cirugía Ortopédica"),
    ("09", "Cirugía Urológica"),
    ("10", "Cirugía de Reconstrucción"),
    ("11", "Cirugía de Tejidos Blandos"),
    ("12", "Cirugía de Tejidos Reproductivos"),
    ("13", "Cirugía de Tumores"),
    ("14", "Cirugía de Vías Respiratorias"),
    ("15", "Cirugía de Vías Urinarias"),
]

VACCINE_TYPE = [
    ("00", "Bacterianas vivas atenuadas"),
    ("01", "Bacterianas inactivadas"),
    ("02", "Inmunidad pasiva"),
    ("03", "Recombinantes"),
    ("04", "Subunitarias"),
    ("05", "Toxoides"),
    ("06", "Víricas vivas atenuadas"),
    ("07", "Víricas inactivadas"),
]

COLOR = [
    ("00", "Amarillo"),
    ("01", "Azul"),
    ("02", "Blanco"),
    ("03", "Gris"),
    ("04", "Marrón"),
    ("05", "Naranja"),
    ("06", "Negro"),
    ("07", "Rojo"),
    ("08", "Verde"),
    ("09", "Rosa"),
]

ATTITUDES = [
    ("00", "Ágil"),
    ("01", "Alerta"),
    ("02", "Amistoso"),
    ("03", "Astuto"),
    ("04", "Cariñoso"),
    ("05", "Caución"),
    ("06", "Dócil"),
    ("07", "Energético"),
    ("08", "Fiel"),
    ("09", "Independiente"),
    ("10", "Inteligente"),
    ("11", "Juguetón"),
    ("12", "Leal"),
    ("13", "Obediente"),
    ("14", "Protector"),
    ("15", "Rápido"),
    ("16", "Reservado"),
    ("17", "Sociable"),
    ("18", "Valiente"),
    ("19", "Versátil"),
]

ALERGY = [
    ("00", "Ácaros del polvo"),
    ("01", "Alimentos"),
    ("02", "Hongos"),
    ("03", "Insectos picadores"),
    ("04", "Moho"),
    ("05", "Pasto"),
    ("06", "Plantas"),
    ("07", "Productos químicos"),
    ("08", "Proteínas de saliva de pulgas"),
    ("09", "Productos de cuidado personal"),
    ("10", "Polen"),
    ("11", "Polvo"),
    ("12", "Medicamentos"),
    ("13", "Pelaje de otros animales"),
    ("14", "Plumas"),
    ("15", "Productos de limpieza y detergentes"),
    ("16", "Sustancias químicas en el entorno "),
    ("17", "Polvo de heno"),
    ("18", "Humo de tabaco"),
    ("19", "Sustancias presentes en juguetes y accesorios para mascotas"),
    ("20", "Virus y bacterias"),
]

EMAIL_REQUIRED = "Se requiere el correo electrónico."
PASSWORD_REQUIRED = "Se requiere la contraseña."
USER_ERROR = "Usuario no encontrado."
OTP_ERROR = "Código OTP incorrecto."
