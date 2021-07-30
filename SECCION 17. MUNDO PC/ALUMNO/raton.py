from DispositivoEntrada import DispositivoEntrada

class Raton(DispositivoEntrada):
    conador_raton = 0

    def __init__(self, tipoEntrada, marca):
        Raton.conador_raton += 1
        super().__init__(tipoEntrada, marca)
        self.IdRaton = Raton.conador_raton

    def __str__(self):
        return f'Raton: [IdRaton: {self.IdRaton}. {super().__str__()}]'

if __name__ == '__main__':
    objRaton = Raton('usb','Hp')
    print(objRaton)