"""
Módulo  : mascota.py
Paquete : entidades
Descripción: Define la clase Mascota con atributos privados,
             getters/setters, __str__ y __len__.
"""


class Mascota:
    """
    Representa a una mascota en el mundo virtual.

    Atributos privados:
        __nombre  (str) : Nombre de la mascota.
        __especie (str) : Tipo de animal.
        __raza    (str) : Raza del animal.
        __edad    (int) : Edad en años.
        __dueno   (str) : Nombre del dueño (ASOCIACIÓN referencia por nombre).
        __trucos  (list): Lista de trucos que sabe la mascota.
    """

    def __init__(self, nombre: str, especie: str, raza: str, edad: int, dueno: str):
        self.__nombre  = nombre
        self.__especie = especie
        self.__raza    = raza
        self.__edad    = edad
        self.__dueno   = dueno
        self.__trucos  = []   # lista interna que crece con la mascota

    # ── Getters ──────────────────────────────────────────────────────────────

    @property
    def nombre(self) -> str:
        return self.__nombre

    @property
    def especie(self) -> str:
        return self.__especie

    @property
    def raza(self) -> str:
        return self.__raza

    @property
    def edad(self) -> int:
        return self.__edad

    @property
    def dueno(self) -> str:
        return self.__dueno

    @property
    def trucos(self) -> list:
        return list(self.__trucos)

    # ── Setters ──────────────────────────────────────────────────────────────

    @nombre.setter
    def nombre(self, valor: str):
        if not valor.strip():
            raise ValueError("El nombre no puede estar vacío.")
        self.__nombre = valor.strip()

    @especie.setter
    def especie(self, valor: str):
        if not valor.strip():
            raise ValueError("La especie no puede estar vacía.")
        self.__especie = valor.strip()

    @raza.setter
    def raza(self, valor: str):
        self.__raza = valor.strip()

    @edad.setter
    def edad(self, valor: int):
        if not isinstance(valor, int) or valor < 0:
            raise ValueError("La edad debe ser un entero no negativo.")
        self.__edad = valor

    @dueno.setter
    def dueno(self, valor: str):
        if not valor.strip():
            raise ValueError("El nombre del dueño no puede estar vacío.")
        self.__dueno = valor.strip()

    # ── Método de negocio ─────────────────────────────────────────────────────

    def aprender_truco(self, truco: str) -> None:
        """Agrega un truco a la lista de habilidades de la mascota."""
        self.__trucos.append(truco.strip())

    # ── Métodos especiales ────────────────────────────────────────────────────

    def __str__(self) -> str:
        trucos_str = ", ".join(self.__trucos) if self.__trucos else "ninguno"
        return (
            f"🐾 MASCOTA\n"
            f"   Nombre    : {self.__nombre}\n"
            f"   Especie   : {self.__especie}\n"
            f"   Raza      : {self.__raza}\n"
            f"   Edad      : {self.__edad} años\n"
            f"   Dueño     : {self.__dueno}\n"
            f"   Trucos    : {trucos_str}"
        )

    def __len__(self) -> int:
        """Retorna la cantidad de trucos que sabe la mascota."""
        return len(self.__trucos)

    def __repr__(self) -> str:
        return f"Mascota(nombre='{self.__nombre}', especie='{self.__especie}')"