

class Monitor:
    conador_Monitor = 0

    def __init__(self,Marca,Tamaño_Monitor):
        Monitor.conador_Monitor += 1
        self.idMonitor = Monitor.conador_Monitor
        self._Marca = Marca
        self._Tamaño_Monitor = Tamaño_Monitor

    @property
    def Marca (self):
        return self._Marca

    @Marca.setter
    def Tipoentrada (self, Marca):
        self._Marca = Marca

    @property
    def Tamaño_Monitor (self):
        return self._Tamaño_Monitor

    @Tamaño_Monitor.setter
    def Tipoentrada (self, Tamaño_Monitor):
        self._Tamaño_Monitor = Tamaño_Monitor

    def __str__(self):
        return f'\nMonitor [IdMonitor: {self.idMonitor}. Marca: {self._Marca}. Tamaño de Monitor: {self._Tamaño_Monitor}]'

if __name__ == '__main__':
    objMonitor = Monitor('DELL','20Pulgadas')
    print(objMonitor)