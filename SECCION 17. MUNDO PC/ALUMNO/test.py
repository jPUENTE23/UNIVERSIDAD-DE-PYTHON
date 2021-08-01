
from Orden import Orden


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