from figura import Figura

PI = 3.14159265358979

class Cilindro(Figura):

    def __init__(self, radio, altura):
        self.radio  = radio
        self.altura = altura

    def volumen(self):
        return PI * self.radio ** 2 * self.altura