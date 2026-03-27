"""
Módulo  : vehiculo.py
Paquete : entidades
Descripción: Define la clase Vehiculo con atributos privados,
             getters/setters, __str__, __len__ y COMPOSICIÓN con Motor.
"""

from entidades.motor import Motor


class Vehiculo:
    """
    Representa un vehículo en el mundo virtual.

    COMPOSICIÓN con Motor: el Motor se crea dentro del Vehículo
    y no existe de forma independiente.

    Atributos privados:
        __marca       (str)   : Marca del vehículo.
        __modelo      (str)   : Modelo específico.
        __anio        (int)   : Año de fabricación.
        __color       (str)   : Color del vehículo.
        __propietario (str)   : Nombre del propietario.
        __motor       (Motor) : Motor del vehículo (COMPOSICIÓN).
        __pasajeros   (list)  : Personas actualmente en el vehículo.
    """

    def __init__(
        self,
        marca: str,
        modelo: str,
        anio: int,
        color: str,
        propietario: str,
        tipo_motor: str = "gasolina",
        cilindrada: float = 1.6,
        caballos_fuerza: int = 120,
    ):
        self.__marca       = marca
        self.__modelo      = modelo
        self.__anio        = anio
        self.__color       = color
        self.__propietario = propietario
        self.__pasajeros   = []

        # COMPOSICIÓN: Motor creado y controlado por Vehiculo
        self.__motor = Motor(tipo_motor, cilindrada, caballos_fuerza)

    # ── Getters ──────────────────────────────────────────────────────────────

    @property
    def marca(self) -> str:
        return self.__marca

    @property
    def modelo(self) -> str:
        return self.__modelo

    @property
    def anio(self) -> int:
        return self.__anio

    @property
    def color(self) -> str:
        return self.__color

    @property
    def propietario(self) -> str:
        return self.__propietario

    @property
    def motor(self) -> Motor:
        return self.__motor

    @property
    def pasajeros(self) -> list:
        return list(self.__pasajeros)

    # ── Setters ──────────────────────────────────────────────────────────────

    @marca.setter
    def marca(self, valor: str):
        if not valor.strip():
            raise ValueError("La marca no puede estar vacía.")
        self.__marca = valor.strip()

    @modelo.setter
    def modelo(self, valor: str):
        if not valor.strip():
            raise ValueError("El modelo no puede estar vacío.")
        self.__modelo = valor.strip()

    @anio.setter
    def anio(self, valor: int):
        if not isinstance(valor, int) or valor < 1886 or valor > 2100:
            raise ValueError("Año de vehículo inválido (1886–2100).")
        self.__anio = valor

    @color.setter
    def color(self, valor: str):
        if not valor.strip():
            raise ValueError("El color no puede estar vacío.")
        self.__color = valor.strip()

    @propietario.setter
    def propietario(self, valor: str):
        if not valor.strip():
            raise ValueError("El propietario no puede estar vacío.")
        self.__propietario = valor.strip()

    # ── Método de negocio ─────────────────────────────────────────────────────

    def subir_pasajero(self, nombre: str) -> None:
        """Sube un pasajero al vehículo."""
        self.__pasajeros.append(nombre.strip())

    # ── Métodos especiales ────────────────────────────────────────────────────

    def __str__(self) -> str:
        pasajeros_str = (
            ", ".join(self.__pasajeros) if self.__pasajeros else "ninguno"
        )
        return (
            f"🚗 VEHÍCULO\n"
            f"   Marca         : {self.__marca}\n"
            f"   Modelo        : {self.__modelo}\n"
            f"   Año           : {self.__anio}\n"
            f"   Color         : {self.__color}\n"
            f"   Propietario   : {self.__propietario}\n"
            f"   Pasajeros     : {pasajeros_str}\n"
            f"   {self.__motor}"
        )

    def __len__(self) -> int:
        """Retorna la cantidad de pasajeros actuales en el vehículo."""
        return len(self.__pasajeros)

    def __repr__(self) -> str:
        return (f"Vehiculo(marca='{self.__marca}', "
                f"modelo='{self.__modelo}', anio={self.__anio})")