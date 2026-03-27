"""
Paquete : entidades
Descripción: Exporta todas las clases del simulador de vida.

Clases disponibles:
    Persona  — persona.py
    Mascota  — mascota.py
    Vehiculo — vehiculo.py
    Motor    — motor.py  (usado internamente por Vehiculo — COMPOSICIÓN)

Relaciones entre clases:
    Composición : Vehiculo  ──▲  Motor   (Motor no existe sin Vehiculo)
    Asociación  : Persona   ──>  Mascota (Persona conoce a su Mascota)
"""

from entidades.motor    import Motor
from entidades.mascota  import Mascota
from entidades.persona  import Persona
from entidades.vehiculo import Vehiculo

__all__ = ["Persona", "Mascota", "Vehiculo", "Motor"]