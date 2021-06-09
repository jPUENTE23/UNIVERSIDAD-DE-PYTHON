
# pedimos los valores
alto = int(input("Ingrese la altura del triangulo: "))
ancho = int(input("Ingrese el anchoo de el triangulo: "))

# hacemos las operaciones correspondientes
area = alto * ancho
perimetro = (alto + ancho)*2

# mostamos los resultados
print("El area del triangulo es: {}".format(area))
print("El perimetro del triangulo es: {}".format(perimetro))