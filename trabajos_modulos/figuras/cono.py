import math
def pedir_valor(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            if valor <= 0:
                print("  El valor debe ser positivo.")
            else:
                return valor
        except ValueError:
            print("  Ingrese un número válido.")

def calcular():
    print("\n--- Cono ---")
    print("Fórmula: V = (1/3) × π × r² × h")
    radio = pedir_valor("  Ingrese el radio de la base (r): ")
    altura = pedir_valor("  Ingrese la altura          (h): ")
    volumen = (1 / 3) * math.pi * radio ** 2 * altura
    print(f"\n  Volumen = {volumen:.4f} unidades³")