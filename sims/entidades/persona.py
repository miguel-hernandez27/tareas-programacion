"""
Módulo  : persona.py
Paquete : entidades
Descripción: Define la clase Persona con atributos privados,
             getters/setters, __str__ y __len__.
"""


class Persona:
    """
    Representa a una persona en el mundo virtual.

    Atributos privados:
        __nombre    (str) : Nombre completo.
        __edad      (int) : Edad en años.
        __ocupacion (str) : Profesión u ocupación.
        __humor     (str) : Estado de ánimo actual.
        __mascotas  (list): Lista de mascotas asociadas (ASOCIACIÓN).
    """

    def __init__(self, nombre: str, edad: int, ocupacion: str, humor: str):
        self.__nombre    = nombre
        self.__edad      = edad
        self.__ocupacion = ocupacion
        self.__humor     = humor
        self.__mascotas  = []   # ASOCIACIÓN: Persona conoce a sus Mascotas

    # ── Getters ──────────────────────────────────────────────────────────────

    @property
    def nombre(self) -> str:
        return self.__nombre

    @property
    def edad(self) -> int:
        return self.__edad

    @property
    def ocupacion(self) -> str:
        return self.__ocupacion

    @property
    def humor(self) -> str:
        return self.__humor

    @property
    def mascotas(self) -> list:
        return list(self.__mascotas)   # copia defensiva

    # ── Setters ──────────────────────────────────────────────────────────────

    @nombre.setter
    def nombre(self, valor: str):
        if not valor.strip():
            raise ValueError("El nombre no puede estar vacío.")
        self.__nombre = valor.strip()

    @edad.setter
    def edad(self, valor: int):
        if not isinstance(valor, int) or valor < 0:
            raise ValueError("La edad debe ser un entero no negativo.")
        self.__edad = valor

    @ocupacion.setter
    def ocupacion(self, valor: str):
        if not valor.strip():
            raise ValueError("La ocupación no puede estar vacía.")
        self.__ocupacion = valor.strip()

    @humor.setter
    def humor(self, valor: str):
        if not valor.strip():
            raise ValueError("El humor no puede estar vacío.")
        self.__humor = valor.strip()

    # ── Asociación: agregar mascota ───────────────────────────────────────────

    def agregar_mascota(self, mascota) -> None:
        """ASOCIACIÓN — vincula una Mascota existente a esta Persona."""
        self.__mascotas.append(mascota)

    # ── Métodos especiales ────────────────────────────────────────────────────

    def __str__(self) -> str:
        mascotas_str = (
            ", ".join(m.nombre for m in self.__mascotas)
            if self.__mascotas else "ninguna"
        )
        return (
            f"👤 PERSONA\n"
            f"   Nombre      : {self.__nombre}\n"
            f"   Edad        : {self.__edad} años\n"
            f"   Ocupación   : {self.__ocupacion}\n"
            f"   Humor       : {self.__humor}\n"
            f"   Mascotas    : {mascotas_str}"
        )

    def __len__(self) -> int:
        """Retorna la cantidad de mascotas asociadas a la persona."""
        return len(self.__mascotas)

    def __repr__(self) -> str:
        return f"Persona(nombre='{self.__nombre}', edad={self.__edad})"