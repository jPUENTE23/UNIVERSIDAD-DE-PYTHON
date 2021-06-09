class Persona:
    # *v nos ayuda a crear una lista
    # **d nos ayuda a crear un diccionario
    def __init__(self, n, e, *v, **d):
        self.nombre = n
        self.edad = e
        self.valores = v
        self.diccionario = d
    def desplegar(self):
        print("Nombre: ", self.nombre)
        print("Edad: ", self.edad)
        print("Valores (Tupla):", self.valores)
        print("Diccionario: ", self.diccionario)

p1 = Persona("Juan", 28)
p1.desplegar()
print()

# guarddamos los valores de la tupla
p2 = Persona("Karla", 30, 2,4,5)
p2.desplegar()
print()

# guardamos los valores de el diccionario
p3 = Persona("Paola", 33, 4,9, m="manzana", p="pera", j="jicama")
p3.desplegar()
