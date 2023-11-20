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