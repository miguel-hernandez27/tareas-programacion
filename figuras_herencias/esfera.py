from figura import Figura

PI = 3.14159265358979

class Esfera(Figura):

    def __init__(self, radio):
        self.radio = radio

    def volumen(self):
        return (4 / 3) * PI * self.radio ** 3