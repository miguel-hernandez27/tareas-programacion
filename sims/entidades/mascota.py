"""
Módulo: mascota.py
Paquete: entidades
Descripción: Define la clase Mascota para el simulador de vida.
"""


class Mascota:
    """
    Clase que representa a una mascota en el mundo virtual.

    Atributos:
        nombre (str): Nombre de la mascota.
        especie (str): Tipo de animal (perro, gato, etc.).
        raza (str): Raza de la mascota.
        edad (int): Edad en años.
        dueno (str): Nombre del dueño.
    """

    def __init__(self, nombre: str, especie: str, raza: str, edad: int, dueno: str):
        self.nombre = nombre
        self.especie = especie
        self.raza = raza
        self.edad = edad
        self.dueno = dueno

    def __str__(self) -> str:
        return (
            f"🐾 MASCOTA\n"
            f"   Nombre    : {self.nombre}\n"
            f"   Especie   : {self.especie}\n"
            f"   Raza      : {self.raza}\n"
            f"   Edad      : {self.edad} años\n"
            f"   Dueño     : {self.dueno}"
        )

    def __repr__(self) -> str:
        return f"Mascota(nombre='{self.nombre}', especie='{self.especie}')"
