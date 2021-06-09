# set es una coleccion sin orden y sin indices, no permite elementos repetidos
# y los elementos no se pueden modificar, pero si agregar nuevos o eliminar

planetas = {"Marte", "Venus","Jupiter"}
print(planetas)

# largo
print(len(planetas))

# revisar si un elemento esta presente
print("Marte" in planetas)

# agregar
planetas.add("Tierra")
print(planetas)
planetas.add("Tierra")  # recordar que en las colecciones set, no nospermite agregar elementos duplicados
print(planetas)

# eliminar elementos posiblemente arroje excepcion
planetas.remove("Tierra")
print(planetas)

# eliminar con discard no arroja excepcion
planetas.discard("Jupiter")
print(planetas)

# limpiar el set
planetas.clear()
print(planetas)

# eliminar set 
del planetas
print(planetas)