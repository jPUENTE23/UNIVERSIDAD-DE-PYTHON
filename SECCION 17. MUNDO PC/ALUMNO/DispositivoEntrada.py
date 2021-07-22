

class DispositivoEntrada :
    def __init__(self,tipoEntrada,marca):
        self._tipoEntrada = tipoEntrada
        self._marca = marca

    @property
    def Tipoentrada (self):
        return self._tipoEntrada

    @Tipoentrada.setter
    def Tipoentrada (self, tipoEntrada):
        self._tipoEntrada = tipoEntrada

    @property
    def Marca (self):
        return self._marca

    @Marca.setter
    def Marca (self, marca):
        self._marca = marca

    def __str__(self):
        return f'Tipo de entrada: {self._tipoEntrada}. Marca: {self._marca}'


if __name__ == '__main__':
    objeto1 = DispositivoEntrada("USB","HP")
    print(objeto1)