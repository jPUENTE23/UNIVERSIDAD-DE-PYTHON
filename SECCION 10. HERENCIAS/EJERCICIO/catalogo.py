

class Vehiculo:
    def __init__(self, Color, Ruedas):
        self.color = Color
        self.ruedas = Ruedas
    def __str__(self):
         return "Color: " + self.color + "\n" "Ruedas: " + str(self.ruedas)

# clase heredadad con la clase Vehiculo
class Coche(Vehiculo):
    def __init__ (self, Color, Ruedas, Velocidad):
        # mandamos a llamar los valores de la clase heredada
        super().__init__(Color, Ruedas)
        self.veloci
    def __str__(self):
        return "Color: " + self.color + "\n" "Ruedas: " + str(self.ruedas) + "\n" "Velocidad: " + self.velocidad

# clase heredadad con la clase Vehiculo
class Bicicleta(Vehiculo):
    def __init__(self, Color, Ruedas, Tipo):
        # mandamos a llamar los valores de la clase heredada
        super().__init__(Color, Ruedas)
        self.tipo = Tipo
    def __str__(self):
         return "Color: " + self.color + "\n" "Ruedas: " + str(self.ruedas) + "\n" "Tipo: " + self.tipo

print("CATALOGO DE ")