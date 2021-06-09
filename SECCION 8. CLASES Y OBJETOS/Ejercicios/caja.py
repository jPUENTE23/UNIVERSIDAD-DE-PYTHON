

class Caja:
    def __init__(self):
        self.ancho = float(input("Ancho de la caja: "))
        self.largo = float(input("Alto de la caja: "))
        self.altura = float(input("Altura de la caja: "))

    def volumenCaje (self):
        self.valumen = self.ancho * self.largo * self.altura
        print("El volumen de la caja es {}".format(self.valumen))

    def verificar(self):
        if self.valumen > 500:
            print("La caja es grande")
        else:
            print("La caja es pequeña")


caja = Caja()
caja.volumenCaje()
caja.verificar()