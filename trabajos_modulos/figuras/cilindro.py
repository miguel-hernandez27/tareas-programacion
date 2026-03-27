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
    print("\n--- Cilindro ---")
    print("Fórmula: V = π × r² × h")
    radio = pedir_valor("  Ingrese el radio  : ")
    altura = pedir_valor(" Ingrese la altura : ")
    volumen =math.pi * radio ** 2 * altura
    print(f"\n  Volumen = {volumen:.4f} unidades³")