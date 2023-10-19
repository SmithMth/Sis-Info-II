class Docente:
    def __init__(self, nombre, titulo, bio, experiencia, educacion):
        self.nombre = nombre
        self.titulo = titulo
        self.bio = bio
        self.experiencia = experiencia
        self.educacion = educacion

# Datos de ejemplo de perfil docente
docente_ejemplo = Docente(
    nombre="Juan Pérez",
    titulo="Profesor de Matemáticas",
    bio="Apasionado por la enseñanza de las matemáticas.",
    experiencia=[
        {"institucion": "Colegio XYZ", "curso": "Álgebra", "fechas": "2018-2022"},
        {"institucion": "Escuela ABC", "curso": "Cálculo", "fechas": "2015-2018"},
    ],
    educacion=[
        {"institucion": "Universidad 123", "titulo": "Licenciatura en Matemáticas", "fecha": "2014"},
        {"institucion": "Universidad 456", "titulo": "Maestría en Educación", "fecha": "2019"},
    ]
)

# Función para mostrar el perfil del docente
def mostrar_perfil(docente):
    print(f"Nombre: {docente.nombre}")
    print(f"Título: {docente.titulo}")
    print(f"Biografía: {docente.bio}")

    print("\nExperiencia Docente:")
    for experiencia in docente.experiencia:
        print(f"- {experiencia['institucion']} - {experiencia['curso']} ({experiencia['fechas']})")

    print("\nFormación Académica:")
    for educacion in docente.educacion:
        print(f"- {educacion['institucion']} - {educacion['titulo']} ({educacion['fecha']})")

# Mostrar el perfil del docente de ejemplo
mostrar_perfil(docente_ejemplo)
