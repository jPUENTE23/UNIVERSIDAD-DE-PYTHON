

class DispositivoEntrada :
    def __init__(self,tipoEntrada,marca):
        self.tipoEntrada = tipoEntrada
        self.marca = marca

    @property
    def Tipoentrada (self):
        return self.tipoEntrada

    @Tipoentrada.setter
    def Tipoentrada (self, tipoEntrada):
        self._apellido = tipoEntrada

    @property
    def Marca (self):
        return self.marca

    @Marca.setter
    def Marca (self, marca):
        self._apellido = marca

    def __str__(self):
        return f'\nTipo de entrada: {self.tipoEntrada}\nMarca: {self.marca}'


if __name__ == '__main__':
    objeto1 = DispositivoEntrada("USB","HP")
    print(objeto1)