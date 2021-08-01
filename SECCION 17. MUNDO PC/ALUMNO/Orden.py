from raton import Raton
from Monitor import Monitor
from teclado import Teclado
from Computadora import Commputadora


class Orden:
    contador_orden = 0

    def __init__(self, orden):
        Orden.contador_orden += 1
        self.id_orden = Orden.contador_orden
        self.orden = orden


    def __str__(self):
        computadora_str = ''
        for computadora in self.orden:
            computadora_str += Commputadora.__str__(self)

        return f'''
        Orden: {self.id_orden}
        Computadora: {computadora_str}
        '''

if __name__ == '__main__':
    objMonitor = Monitor('Lenovo','18 Pulgadas')
    objTeclado = Teclado('usb','hp')
    objRaton = Raton('usb','logitech')
    objCompu1 = Commputadora('Gamer',objMonitor,objTeclado,objRaton)

    objMonitor = Monitor('Lenovo','18 Pulgadas')
    objTeclado = Teclado('usb','hp')
    objRaton = Raton('usb','logitech')
    objCompu2 = Commputadora('Gamer',objMonitor,objTeclado,objRaton)

    lista = [objCompu1,objCompu2]

    objOrden = Orden(lista)
    print(objOrden)