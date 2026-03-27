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
    print("\---Cubo---")
    print("Fórmula: V = a³")
    a = pedir_valor("  Ingrese el lado (a): ")
    volumen = a ** 3
    print(f"\n  Volumen = {volumen:.4f} unidades³")