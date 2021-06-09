
class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def areaRectangulo (self):
        return self.base * self.altura

base = int(input("Dame la base de el rectangulo: "))
altura = int(input("Dame la altura de el rectangulo: "))

rectangulo = Rectangulo(base,altura)
print("El area del rectangulo es {} ".format(rectangulo.areaRectangulo()))