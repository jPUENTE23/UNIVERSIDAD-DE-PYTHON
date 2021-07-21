

class Teclado:
    Contador_Teclado = 0

    def __init__(self):
        Teclado.Contador_Teclado += 1
        self.idTeclado = Teclado.Contador_Teclado

    def __str__(self):
        return f'\nIdTeclado: {self.idTeclado}'

if __name__ == '__main__':
    objteclado = Teclado()
    print(objteclado)
