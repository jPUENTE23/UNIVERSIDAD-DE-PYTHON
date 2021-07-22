from raton import Raton
from Monitor import Monitor
from teclado import Teclado

class Commputadora(Monitor,Teclado,Raton):
    conattador_Compuadora = 0

    def __init__(self, nombre, marcaMonitor, tamMonitor, tipoEntradaTeclado, marcaTeclado, tipoEntradaRaton, marcaRaton):
        Commputadora.conattador_Compuadora += 1
        Monitor.__init__(self,marcaMonitor,tamMonitor)
        Teclado.__init__(self,tipoEntradaTeclado, marcaTeclado)
        Raton.__init__(self,tipoEntradaRaton,marcaRaton)
        self.idComputadora = Commputadora.conattador_Compuadora
        self._nombre = nombre

    @property
    def Nombre (self):
        return self._nombre

    @Nombre.setter
    def Nombre (self, nombre):
        self._nombre = nombre


    def __str__(self):
        return f'\n{self._nombre} : {self.idComputadora}\n{Monitor.__str__(self)}\n{Teclado.__str__(self)}\n{Raton.__str__(self)}'


if __name__ == '__main__':
    objCompu = Commputadora('Gamer','LG','20 Pulgadas','usb','Logitch','Bluetooh','Microsoft')
    print(objCompu)