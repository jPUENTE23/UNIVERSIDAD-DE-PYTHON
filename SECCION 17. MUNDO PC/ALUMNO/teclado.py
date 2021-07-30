from DispositivoEntrada import DispositivoEntrada

class Teclado(DispositivoEntrada):
    Contador_Teclado = 0

    def __init__(self, tipoEntrada, marca):
        Teclado.Contador_Teclado += 1
        super().__init__(tipoEntrada, marca)
        self.idTeclado = Teclado.Contador_Teclado

    def __str__(self):
        return f'Teclado: [IdTeclado: {self.idTeclado}. {super().__str__()}]'

if __name__ == '__main__':
    objteclado = Teclado('usb','Lenovo')
    print(objteclado)
