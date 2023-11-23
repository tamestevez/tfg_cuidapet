from .utils import get_constants


NATIONALITY=[
   (country['cca2'], country['translations']['spa']['common']) for country in get_constants('nationalities')
]

SEX=[
    ("F", "FEMIA"),
    ("M", "MACHO"),
]

ROLE=[
    ("PROP", "PROPIETARIO"),
    ("PROT", "PROTECTORA"),
    ("ADMI", "ADMINISTRADOR"), 
    ("CLIN","CLINICA"), 
]


SPECIE=(
    ('Perro', [
        (dog['name'], dog['name']) for dog in get_constants('dogs')] if get_constants('dogs') else [('Perro', 'Perro')
    ]),
    ('Gato', [
        (dog['name'], dog['name']) for dog in get_constants('cats')] if get_constants('cats') else [('Perro', 'Perro')
    ]),
    ('Exótico', [
        ('ARAÑA', 'Araña'),
        ('CHINCHILLA', 'Chinchilla'),
        ('COBAYA', 'Cobaya'),
        ('ERIZO', 'Erizo'),
        ('HURON', 'Hurón'),
        ('PEZ', 'Pez'),
        ('REPTIL', 'Reptil'),
    ]),
    ('Otros', [
        ('AVE', 'Ave'),
        ('BOVINO', 'Bovino'),
        ('CABALLO', 'Caballo'),
        ('CERDO', 'Cerdo'), 
        ('CONEJO', 'Conejo'),
        ('OTRO', 'Otro'),
    ]),
)

TOWN=[
    (town['codigo'], town['provincia']) for town in get_constants('towns')['results']
]

MARKING_TYPE=[
    ("00", "Anilla"),
    ("01","Branding"),
    ("02", "Collar de seguimiento"),
    ("03", "Etiqueta"),
    ("04", "Marca"),
    ("05", "Microchip"),
    ("06", "Tatuaje"),
    ("07", "Tinta"),
]

DEATH_CAUSE=[
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