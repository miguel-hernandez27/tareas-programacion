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
    print("\n--- Paralelepípedo ---")
    print("Fórmula: V = largo x ancho x altura")
    largo = pedir_valor("  Ingrese el largo : ")
    ancho = pedir_valor("  Ingrese el ancho : ")
    altura = pedir_valor("  Ingrese el alto : ")
    volumen = largo * ancho * altura
    print(f"\n  Volumen = {volumen:.4f} unidades³")