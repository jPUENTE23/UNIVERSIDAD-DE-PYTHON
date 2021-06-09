class Persona:
    def __init__(self, nombre, ape_paterno, ape_materno):
        # atributo publico
        self.nombre = nombre
        # atributo parcialmente privado
        self._apellido_paterno = ape_paterno
        # atributo privado
        self.__apellido_materno = ape_materno

    def metodo_publico(self):
        self.__metodo_privado()

    # si nosostros mandamos a llamar el metodo privado, nos marcara error ya que este no se puede visualizar
    # para eso creamos el metodo publico y mandamos a llamar el metodo privado
    def __metodo_privado(self):
        print(self.nombre)
        print(self._apellido_paterno)
        print(self.__apellido_materno)

    def get_apellido_materno(self):
        return self.__apellido_materno

    def set_apellido_materno(self, ape_materno):
        self.__apellido_materno = ape_materno

    def get_apeMaterno(self):
        return self.__apellido_materno

p1 = Persona("Juan", "Lopez", "Perez")
#p1.__metodo_privado() no se puede acceder debido a que es privado
p1.metodo_publico()
print("")
print(p1.nombre)
print(p1._apellido_paterno)
#print(p1.__apellido_materno) manda un error por ser privado
print(p1.get_apeMaterno())
