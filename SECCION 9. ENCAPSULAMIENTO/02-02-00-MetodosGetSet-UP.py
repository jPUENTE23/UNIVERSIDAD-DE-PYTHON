

class Persona:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    # METODO GET
    # El metodo get lo que hara es obtener el valor encapsulado para
    # poder mostararlo al usuario
    @property
    def nombre(self):
        return self._nombre

    # METODO SET
    # El set no auyudara a en caso de que queramos modificar un valor de un atributo encapsulado
    # De lo contarrio si no lo  queremos modificar, solo omitmos las lineas correspondientes
    # La diferencia de setter es que llevara un parametro para que obtenga el valor a modificar

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    # Ahora agregamos los metodos get y set para los siguientes atributos encapsulados
    # Atributo _apellido
    @property
    def apellido(self):
        return self.apellido
    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    # Atributo _edad
    @property
    def edad(self):
        return self.edad
    @edad.setter
    def edad(self, edad):
        self._edad = edad
    def mostrar_detalle(self):
        print(f'Persona: {self._nombre} {self._apellido} {self._edad}')

persona1 = Persona('Juan', 'Perez', 28)
persona1.nombre = 'Jorge Luis'
persona1.apellido = 'Puente Muñiz'
persona1.edad = 19
persona1.mostrar_detalle()
#print(persona1.nombre)
# persona1._nombre = 'Cambio'
# print(persona1._nombre)