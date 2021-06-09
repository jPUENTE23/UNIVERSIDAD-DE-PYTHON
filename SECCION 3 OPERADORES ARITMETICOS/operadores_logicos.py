
numMin = 0
numMax = 5

num = int(input("Ingresas un numero: "))
rango = (num >= numMin and num <= numMax)
if (rango):
    print("EStas dentro del rango")
else:
    print("Estas fuera del rango")