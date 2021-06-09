
grupo = "BMTH"

# estas son las diferentes formas que podemos utilizar para
# imprimir en pantalla una cadena junto con una variable
print("Mi grupo favorito es: {0}".format(grupo))
print("Mi grupo favorito es:",grupo)
print("Mi grupo favorito es:" + grupo)

# una cadena no puede sumer numeros
# ejemplo

num1 = "1"
num2 = "2"
print("La suma es...{}".format(num1 + num2))

num1 = 1
num2 = 2
print("La suma es...{}".format(num1 + num2))

# si intentas imprimir un suma con este metodo de concatenacion
# marcara error ya que se no puede concatenar una cadena de texto con un volor int
# SOLO SI IMPRIMES DE ESTA MANERA
# print("La suma es..." + num1 + num2)

print("La suma es..." + str(num1 + num2))

