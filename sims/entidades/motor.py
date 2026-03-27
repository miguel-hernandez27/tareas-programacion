"""
Módulo  : motor.py
Paquete : entidades
Descripción: Define la clase Motor.
             Usada como COMPOSICIÓN dentro de Vehiculo:
             un Motor no existe sin su Vehículo.
"""


class Motor:
    """
    Representa el motor de un vehículo.

    Atributos privados:
        __tipo         (str)   : Tipo de motor (gasolina, eléctrico, híbrido).
        __cilindrada   (float) : Cilindrada en litros.
        __caballos_fuerza (int): Potencia en HP.
    """

    def __init__(self, tipo: str, cilindrada: float, caballos_fuerza: int):
        self.__tipo            = tipo
        self.__cilindrada      = cilindrada
        self.__caballos_fuerza = caballos_fuerza

    # ── Getters ──────────────────────────────────────────────────────────────

    @property
    def tipo(self) -> str:
        return self.__tipo

    @property
    def cilindrada(self) -> float:
        return self.__cilindrada

    @property
    def caballos_fuerza(self) -> int:
        return self.__caballos_fuerza

    # ── Setters ──────────────────────────────────────────────────────────────

    @tipo.setter
    def tipo(self, valor: str):
        opciones = {"gasolina", "diesel", "eléctrico", "híbrido"}
        if valor.lower() not in opciones:
            raise ValueError(f"Tipo de motor inválido. Opciones: {opciones}")
        self.__tipo = valor.lower()

    @cilindrada.setter
    def cilindrada(self, valor: float):
        if valor <= 0:
            raise ValueError("La cilindrada debe ser mayor a 0.")
        self.__cilindrada = valor

    @caballos_fuerza.setter
    def caballos_fuerza(self, valor: int):
        if valor <= 0:
            raise ValueError("Los caballos de fuerza deben ser > 0.")
        self.__caballos_fuerza = valor

    # ── Métodos especiales ────────────────────────────────────────────────────

    def __str__(self) -> str:
        return (
            f"⚙️  MOTOR\n"
            f"      Tipo          : {self.__tipo}\n"
            f"      Cilindrada    : {self.__cilindrada} L\n"
            f"      Caballos      : {self.__caballos_fuerza} HP"
        )

    def __len__(self) -> int:
        """Retorna los caballos de fuerza como medida de 'tamaño' del motor."""
        return self.__caballos_fuerza

    def __repr__(self) -> str:
        return (f"Motor(tipo='{self.__tipo}', "
                f"cilindrada={self.__cilindrada}, "
                f"hp={self.__caballos_fuerza})")