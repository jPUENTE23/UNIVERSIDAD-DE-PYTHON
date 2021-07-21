

class Raton:
    conador_raton = 0

    def __init__(self):
        Raton.conador_raton += 1
        self.IdRaton = Raton.conador_raton

    def __str__(self):
        return f'\nIdRaton: {self.IdRaton}'

if __name__ == '__main__':
    objRaton = Raton()
    print(objRaton)