
class Aritmetica:
    def __init__(self, operando1, operando2):
        self.operando1 = operando1
        self.operando2 = operando2

    def suma (self):
        return self.operando1 + self.operando2

    def resta (self):
        return self.operando1 - self.operando2

aritmetica = Aritmetica(20,30)
print("La suma es {}".format(aritmetica.suma()))
print("La resta es {} ".format(aritmetica.resta()))