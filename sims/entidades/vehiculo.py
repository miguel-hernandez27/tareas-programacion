"""
Módulo: vehiculo.py
Paquete: entidades
Descripción: Define la clase Vehiculo para el simulador de vida.
"""


class Vehiculo:
    """
    Clase que representa un vehículo en el mundo virtual.

    Atributos:
        marca (str): Marca del vehículo.
        modelo (str): Modelo específico.
        anio (int): Año de fabricación.
        color (str): Color del vehículo.
        propietario (str): Nombre del propietario.
    """

    def __init__(self, marca: str, modelo: str, anio: int, color: str, propietario: str):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.color = color
        self.propietario = propietario

    def __str__(self) -> str:
        return (
            f"🚗 VEHÍCULO\n"
            f"   Marca       : {self.marca}\n"
            f"   Modelo      : {self.modelo}\n"
            f"   Año         : {self.anio}\n"
            f"   Color       : {self.color}\n"
            f"   Propietario : {self.propietario}"
        )

    def __repr__(self) -> str:
        return f"Vehiculo(marca='{self.marca}', modelo='{self.modelo}', anio={self.anio})"
