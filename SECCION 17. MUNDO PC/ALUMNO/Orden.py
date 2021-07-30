from raton import Raton
from Monitor import Monitor
from teclado import Teclado
from Computadora import Commputadora


class Orden:
    contador_orden = 0

    def __init__(self, orden):
        Orden.contador_orden += 1
        self.id_orden = Orden.contador_orden
        self.orden = list(orden)


    def __str__(self):
        return f'''
        {self.id_orden}
        {self.orden}
        '''

if __name__ == '__name__':
    objMonitor = Monitor('Lenovo','18 Pulgadas')
    objTeclado = Teclado('usb','hp')
    objRaton = Raton('usb','logitech')
    objCompu1 = Commputadora('Gamer',objMonitor,objTeclado,objRaton)
    objCompu2 = Commputadora('Gamer',objMonitor,objTeclado,objRaton)
    ListaOrden = [objCompu1, objCompu1]
    objOrden = Orden(ListaOrden)
    print(objOrden)