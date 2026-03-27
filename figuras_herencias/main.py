from figura         import Figura
from cubo           import Cubo
from paralelepipedo import Paralelepipedo
from cilindro       import Cilindro
from esfera         import Esfera
from cono           import Cono


# ─── Principio de Sustitución de Liskov ───────────────────────────────────────
def imprimir_volumen(figura: Figura):
    print(f"\n  Volumen = {figura.volumen():.4f} unidades³")


figuras = {
    1: ("Cubo              (l=5)",           Cubo(5)),
    2: ("Paralelepípedo    (l=4, a=3, h=6)", Paralelepipedo(4, 3, 6)),
    3: ("Cilindro          (r=3, h=7)",      Cilindro(3, 7)),
    4: ("Esfera            (r=4)",           Esfera(4)),
    5: ("Cono              (r=3, h=5)",      Cono(3, 5)),
}


# ─── Menú ──────────────────────────────────────────────────────────────────────
def mostrar_menu():
    print("\n" + "=" * 40)
    print("     CALCULADORA DE VOLÚMENES - POO")
    print("=" * 40)
    for numero, (descripcion, _) in figuras.items():
        print(f"  {numero}. Volumen del {descripcion}")
    print("  6. Salir")
    print("=" * 40)


def main():
    while True:
        mostrar_menu()

        try:
            opcion = int(input("\n  Seleccione una opción: "))
        except ValueError:
            print("\n  Ingrese un número válido.")
            continue

        if opcion == 6:
            print("\n  Hasta luego!\n")
            break
        elif opcion in figuras:
            descripcion, figura = figuras[opcion]
            print(f"\n  --- {descripcion} ---")
            imprimir_volumen(figura)
            input("\n  Presione Enter para continuar...")
        else:
            print("\n  Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    main()