
# tupla matiene el orden, pero ya nose pueden modificar.
frutas = ("Naranja","Platano","Guayaba")
print(frutas)

# largo de la tupla
print(len(frutas))

# acceder a un elemento
print(frutas[1])

# navegacion inversa
print(frutas[-1])

# rangos
print(frutas[0:2])

# convertir una tupla a una lista
_frutas = list(frutas)
_frutas[1] = "Manzana"

# convertimos la lista a una tupla nuevamente
frutas = tuple(_frutas)
print(frutas)

# iterar con una tupla
for frut in frutas:
    print(frut, end = " - ")

# recordar que en una tupla no podemos agregar ni borrar un elemento