from figura import Figura

class Cubo(Figura):

    def __init__(self, lado):
        self.lado = lado

    def volumen(self):
        return self.lado ** 3