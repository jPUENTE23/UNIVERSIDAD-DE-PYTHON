

class Pelicula:
    def __init__(self, NOmbre):
        self._Nombre = NOmbre

    @property
    def Nombre (self):
        return self._Nombre

    @Nombre.setter
    def Nombre (self, Nombre):
        self._Nombre = self.Nombre

    def __str__(self):
        return f"{self._Nombre}"

if __name__ == "__main__":
    MyObject = Pelicula("Dune")
    print(MyObject)
    print(MyObject._Nombre)

    MyObject._Nombre = "Venom"
    print(MyObject._Nombre)