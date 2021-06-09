
def suma (a=0,b=0):
    # return lo que hara es devolvernos el resultado de la suma a+b
    return a+b;

# pero para que return nos devuelvo el resultado que delcarar los valores
# dentro de los argumentos de nuestra funcion
print("El resultado es {}".format(suma(3,3)))

# si no mandamos valores s nuestros argumentos
# al momneto de ejecutar el programa nos marcara una excepcion
# para evitar eso podemos asignarle valores por default a nuestros parametros
print("El resultado es {}".format(suma()))