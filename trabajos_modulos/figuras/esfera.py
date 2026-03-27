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
    print("\n--- Esfera ---")
    print("Fórmula: V = (4/3) × π × r³")
    radio = pedir_valor("  Ingrese el radio (r): ")
    volumen = (4 / 3) * math.pi * radio ** 3
    print(f"\n  Volumen = {volumen:.4f} unidades³")