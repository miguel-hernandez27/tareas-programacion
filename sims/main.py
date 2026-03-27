"""
Programa principal: main.py
Descripción: Punto de entrada del Simulador de Vida — Sims World.
             Importa módulos y paquetes para gestionar entidades.

Estructura del proyecto:
    sims_world/
    ├── main.py              ← Programa principal
    ├── menu.py              ← Módulo de interfaz de menú
    ├── gestor.py            ← Módulo de gestión de entidades
    └── entidades/           ← Paquete de clases
        ├── __init__.py
        ├── persona.py
        ├── mascota.py
        └── vehiculo.py
"""

from menu import mostrar_menu, solicitar_opcion
import gestor


ACCIONES = {
    "1": gestor.crear_persona,
    "2": gestor.crear_mascota,
    "3": gestor.crear_vehiculo,
    "4": gestor.imprimir_personas,
    "5": gestor.imprimir_mascotas,
    "6": gestor.imprimir_vehiculos,
    "7": gestor.imprimir_todas,
}


def main() -> None:
    """Función principal: ejecuta el bucle del simulador."""
    print("\n  🌍 Bienvenido al Simulador de Vida — Sims World")

    while True:
        mostrar_menu()
        opcion = solicitar_opcion()

        if opcion == "0":
            print("\n  👋 ¡Hasta pronto! Saliendo del simulador...\n")
            break
        elif opcion in ACCIONES:
            ACCIONES[opcion]()
        else:
            print("  ⚠️  Opción inválida. Por favor elija una opción del menú.")


if __name__ == "__main__":
    main()
