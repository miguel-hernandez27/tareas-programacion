from figuras import cubo, paralelepipedo, cilindro, esfera, cono

MENU = [
    (1, "Cubo", cubo.calcular),
    (2, "Paralelepípedo", paralelepipedo.calcular),
    (3, "Cilindro", cilindro.calcular),
    (4, "Esfera", esfera.calcular),
    (5, "Cono", cono.calcular)
]

def mostrar_menu():
    print("\n" + "=" * 40)
    print("   CALCULADORA DE VOLÚMENES ")
    print("=" * 40)
    for num, nombre, _ in MENU:
        print(f"  {num}. {nombre}")
    print("  0. Salir")
    print("=" * 40)

def main():
    while True:
        mostrar_menu()
        try:
            opcion = int(input("\n  Seleccione una figura: "))
        except ValueError:
            print("\n  Ingrese un número válido.")
            continue

        if opcion == 0:
            print("\n  Hasta luego!\n")
            break
        elif 1 <= opcion <= len(MENU):
            _, _, funcion = MENU[opcion - 1]
            funcion()
            input("\n  Presione Enter para continuar...")
        else:
            print("\n  Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()