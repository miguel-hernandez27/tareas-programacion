from figura import Figura

PI = 3.14159265358979

class Cono(Figura):

    def __init__(self, radio, altura):
        self.radio  = radio
        self.altura = altura

    def volumen(self):
        return (1 / 3) * PI * self.radio ** 2 * self.altura