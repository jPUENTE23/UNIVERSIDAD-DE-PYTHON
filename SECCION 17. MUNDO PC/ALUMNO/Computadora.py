from raton import Raton
from Monitor import Monitor
from teclado import Teclado

class Commputadora:
    conattador_Compuadora = 0

    def __init__(self, nombre, monitor, taclado, raton):
        Commputadora.conattador_Compuadora += 1
        self._nombre = nombre
        self._monitor = monitor
        self._teclado = Teclado
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
    def Monitor (self, monitor):
        self._monitor = monitor

    @property
    def Teclado (self):
        return self._teclado

    @Teclado.setter
    def Teclado (self, teclado):
        self._teclado = teclado

    @property
    def raton (self):
        return self._raton

    @raton.setter
    def raton (self, raton):
        self._raton = raton