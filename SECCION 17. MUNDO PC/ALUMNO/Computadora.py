from raton import Raton
from Monitor import Monitor
from teclado import Teclado

class Commputadora:
    conattador_Compuadora = 0

    def __init__(self, nombre, monitor, teclado, raton):
        Commputadora.conattador_Compuadora += 1
        self.id_Computadora = Commputadora.conattador_Compuadora
        self._nombre = nombre
        self._monitor = monitor
        self._teclado = teclado
        self._raton = raton

    @property
    def Nombre (self):
        return self._nombre

    @Nombre.setter
    def Nombre (self, nombre):
        self._nombre = nombre

    @property
    def Monitor (self):
        return self._monitor

    @Monitor.setter
    def Nombre (self, monitor):
        self._monitor = monitor

    @property
    def Teclado (self):
        return self._teclado

    @Teclado.setter
    def Nombre (self, teclado):
        self._teclado = teclado

    @property
    def Raton (self):
        return self._raton

    @Raton.setter
    def Nombre (self, raton):
        self._raton = raton


    def __str__(self):
        return f''''
        {self._nombre}:{self.id_Computadora}
        {self._monitor}
        {self._teclado}
        {self._raton}
        '''


if __name__ == '__main__':
    objMonitor = Monitor('Lenovo','18 Pulgadas')
    objTeclado = Teclado('usb','hp')
    objRaton = Raton('usb','logitech')
    objCompu1 = Commputadora('Gamer',objMonitor,objTeclado,objRaton)
    print(objCompu1)