"""
Módulo: gestor.py
Descripción: Gestiona la creación y visualización de entidades del simulador.
             Contiene las listas de personas, mascotas y vehículos.
"""

from entidades import Persona, Mascota, Vehiculo
from menu import titulo_seccion, separador

# ─── Listas de almacenamiento ────────────────────────────────────────────────
personas: list[Persona] = []
mascotas: list[Mascota] = []
vehiculos: list[Vehiculo] = []


# ─── Funciones de creación ───────────────────────────────────────────────────

def crear_persona() -> None:
    """Solicita datos al usuario y crea una nueva Persona."""
    titulo_seccion("✏️  CREAR NUEVA PERSONA")
    try:
        nombre    = input("   Nombre     : ").strip()
        edad      = int(input("   Edad       : "))
        ocupacion = input("   Ocupación  : ").strip()
        humor     = input("   Humor      : ").strip()

        if not nombre:
            print("   ⚠️  El nombre no puede estar vacío.")
            return

        persona = Persona(nombre, edad, ocupacion, humor)
        personas.append(persona)
        print(f"\n   ✅ ¡Persona '{nombre}' creada exitosamente!")
    except ValueError:
        print("   ❌ Error: la edad debe ser un número entero.")


def crear_mascota() -> None:
    """Solicita datos al usuario y crea una nueva Mascota."""
    titulo_seccion("✏️  CREAR NUEVA MASCOTA")
    try:
        nombre  = input("   Nombre    : ").strip()
        especie = input("   Especie   : ").strip()
        raza    = input("   Raza      : ").strip()
        edad    = int(input("   Edad      : "))
        dueno   = input("   Dueño     : ").strip()

        if not nombre:
            print("   ⚠️  El nombre no puede estar vacío.")
            return

        mascota = Mascota(nombre, especie, raza, edad, dueno)
        mascotas.append(mascota)
        print(f"\n   ✅ ¡Mascota '{nombre}' creada exitosamente!")
    except ValueError:
        print("   ❌ Error: la edad debe ser un número entero.")


def crear_vehiculo() -> None:
    """Solicita datos al usuario y crea un nuevo Vehículo."""
    titulo_seccion("✏️  CREAR NUEVO VEHÍCULO")
    try:
        marca       = input("   Marca       : ").strip()
        modelo      = input("   Modelo      : ").strip()
        anio        = int(input("   Año         : "))
        color       = input("   Color       : ").strip()
        propietario = input("   Propietario : ").strip()

        if not marca:
            print("   ⚠️  La marca no puede estar vacía.")
            return

        vehiculo = Vehiculo(marca, modelo, anio, color, propietario)
        vehiculos.append(vehiculo)
        print(f"\n   ✅ ¡Vehículo '{marca} {modelo}' creado exitosamente!")
    except ValueError:
        print("   ❌ Error: el año debe ser un número entero.")


# ─── Funciones de impresión ──────────────────────────────────────────────────

def imprimir_personas() -> None:
    """Muestra todas las personas registradas."""
    titulo_seccion(f"📋 PERSONAS REGISTRADAS  [{len(personas)}]")
    if not personas:
        print("   (No hay personas registradas aún)")
        return
    for i, p in enumerate(personas, 1):
        print(f"\n   [{i}] {p}")
        separador()


def imprimir_mascotas() -> None:
    """Muestra todas las mascotas registradas."""
    titulo_seccion(f"📋 MASCOTAS REGISTRADAS  [{len(mascotas)}]")
    if not mascotas:
        print("   (No hay mascotas registradas aún)")
        return
    for i, m in enumerate(mascotas, 1):
        print(f"\n   [{i}] {m}")
        separador()


def imprimir_vehiculos() -> None:
    """Muestra todos los vehículos registrados."""
    titulo_seccion(f"📋 VEHÍCULOS REGISTRADOS  [{len(vehiculos)}]")
    if not vehiculos:
        print("   (No hay vehículos registrados aún)")
        return
    for i, v in enumerate(vehiculos, 1):
        print(f"\n   [{i}] {v}")
        separador()


def imprimir_todas() -> None:
    """Muestra todas las entidades registradas en el sistema."""
    total = len(personas) + len(mascotas) + len(vehiculos)
    titulo_seccion(f"🌍 TODAS LAS ENTIDADES  [Total: {total}]")
    imprimir_personas()
    imprimir_mascotas()
    imprimir_vehiculos()
