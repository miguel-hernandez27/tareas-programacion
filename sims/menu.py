"""
Módulo: menu.py
Descripción: Gestiona la visualización del menú y la interacción con el usuario.
"""

LINEA = "═" * 50
LINEA_FINA = "─" * 50


def mostrar_menu() -> None:
    """Despliega el menú principal del simulador."""
    print(f"\n{'╔' + LINEA + '╗'}")
    print(f"║{'🌍  SIMULADOR DE VIDA  —  SIMS WORLD':^50}║")
    print(f"{'╠' + LINEA + '╣'}")
    print(f"║  {'CREAR':}{'':33}║")
    print(f"║   1. 👤 Crear Persona{'':28}║")
    print(f"║   2. 🐾 Crear Mascota{'':28}║")
    print(f"║   3. 🚗 Crear Vehículo{'':27}║")
    print(f"{'╠' + LINEA + '╣'}")
    print(f"║  {'VISUALIZAR':}{'':39}║")
    print(f"║   4. 📋 Imprimir Personas{'':24}║")
    print(f"║   5. 📋 Imprimir Mascotas{'':24}║")
    print(f"║   6. 📋 Imprimir Vehículos{'':23}║")
    print(f"║   7. 📋 Imprimir Todas las Entidades{'':12}║")
    print(f"{'╠' + LINEA + '╣'}")
    print(f"║   0. 🚪 Salir{'':36}║")
    print(f"{'╚' + LINEA + '╝'}")


def solicitar_opcion() -> str:
    """Solicita y retorna la opción elegida por el usuario."""
    return input("\n  👉 Seleccione una opción: ").strip()


def titulo_seccion(titulo: str) -> None:
    """Imprime un encabezado decorativo para una sección."""
    print(f"\n  ┌{LINEA_FINA}┐")
    print(f"  │ {titulo:<48} │")
    print(f"  └{LINEA_FINA}┘")


def separador() -> None:
    print(f"  {LINEA_FINA}")
