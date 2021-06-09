nombre = ["Jorge","Luis","Puente","Muñiz"]
print(nombre)

# conocer el largo de la lista
print("La lista tiene {} palabras".format(len(nombre)))

# conocer el indice de cualquier elemento de una lista
print(nombre[1])
print(nombre[2])

# navegacion inversa
print(nombre[-1])
print(nombre[-2])

# imprimir rango 
print(nombre[0:3])

# imprimir los elementos de icnicio hasta el indice indicado
print(nombre[:2])

# imprimir los elemntos hasta el final hasta el indice proporcionado
print(nombre[2:])

# cambiar los elementos de una lista
nombre[2] = "Antonio"
print(nombre)

# iterar una lista
for _nombre in nombre:
    print(_nombre)

# revisar si existe un elemento en una lista
if "Edgar" in nombre:
    print("El nombre si se encuentra registrado")
else:
    print("El nombre no se encuentra en la lista")

# agragar un nuevo elemento
nombre.append("Karla")
print(nombre)

# insertar un elemento en un indice proporcionado
nombre.insert(3, "Cecy")
print(nombre)

# remover un elemento
nombre.remove("Muñiz")
print(nombre)

# remover el ultimo elemento de la lista
nombre.pop()
print(nombre)

# remover el indice indicado de la lista
# si no indicamos el indice del elemento que se va a remover en la lista
# removera la lista completa
del nombre[0]
print(nombre)

# limpiar los elementos de una lista
nombre.clear()
print(nombre)

# eliminar por completo la lista
del nombre
print(nombre)