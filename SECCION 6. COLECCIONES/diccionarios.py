# un diccionario esta compuesto de llave y valor (key, value)
# un diccionario no tiene un indice numerico
diccionario = {
    "IDE": "Integrated Development Enviroment",
    "OPP": "Object Oriented Programing",
    "DBMS":"Database Management System"
}

print(diccionario)

# largo de un diccionario
print(len(diccionario))

# acceder a un elemento con la llave del diccionario
print(diccionario["IDE"])

# otra forma de accedr a un elemento en le diccionario
print(diccionario.get("IDE"))

# modificar un elemento
diccionario["IDE"] = "sin valor alguno"
print(diccionario)

# iterar un diccionario
# al momento de iterar un diccionario con un for, solo nos devolvera las llaves del diccionario
for termino in diccionario:
    print(termino)
# con la sig iteracion nos devvolvera el valor de cada llave del diccionario
for termino in diccionario:
    print(diccionario[termino])

# otra forma de acceder a los valores
for valores in diccionario.values():
    print(valores)

# comprobar existencia de un elemento en el diccionario
print("IDE" in diccionario)

# agregar nuevos elementos
diccionario["PK"] = "Primary Key"
print(diccionario)

# remover un elemento del diccionario
diccionario.pop("DBMS")
print(diccionario)

# limpiar diccionario
diccionario.clear()
print(diccionario)

# eliminar diccionario
del diccionario
print(diccionario)