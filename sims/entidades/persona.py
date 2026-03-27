"""
Módulo: persona.py
Paquete: entidades
Descripción: Define la clase Persona para el simulador de vida.
"""


class Persona:
    """
    Clase que representa a una persona en el mundo virtual.

    Atributos:
        nombre (str): Nombre de la persona.
        edad (int): Edad de la persona.
        ocupacion (str): Ocupación o profesión.
        humor (str): Estado de ánimo actual.
    """

    def __init__(self, nombre: str, edad: int, ocupacion: str, humor: str):
        self.nombre = nombre
        self.edad = edad
        self.ocupacion = ocupacion
        self.humor = humor

    def __str__(self) -> str:
        return (
            f"👤 PERSONA\n"
            f"   Nombre    : {self.nombre}\n"
            f"   Edad      : {self.edad} años\n"
            f"   Ocupación : {self.ocupacion}\n"
            f"   Humor     : {self.humor}"
        )

    def __repr__(self) -> str:
        return f"Persona(nombre='{self.nombre}', edad={self.edad})"
