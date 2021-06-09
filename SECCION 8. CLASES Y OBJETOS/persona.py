
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad


# creamos el objeto
persona = Persona("Jorge",19)
# mandamos a llmar el objeto
print("El nombre de la persona es: {} ".format(persona.nombre))
print("Y tiene {} años ".format(persona.edad))

# creamos un segundo objeto
persona2 = Persona("Luis",19)
print("El nombre de la persona es: {} ".format(persona2.nombre))
print("Y tiene {} años ".format(persona2.edad))