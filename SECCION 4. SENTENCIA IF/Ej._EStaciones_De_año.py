
mes = int(input("Ingrese el mes que desee ver (1-12): "))

if mes == 1 or mes == 2 or mes ==12:
    estacion = "Invierno"
    print("La estacion del mes es {}".format(estacion))
elif mes == 3 or mes == 4 or mes == 5:
    estacion = "Primavera"
    print("La estacion del mes es {}".format(estacion))
elif mes == 6 or mes == 7 or mes == 8 or mes == 9:
    estacion = "Verano"
    print("La estacion del mes es {}".format(estacion))
elif mes == 10 or mes == 11:
    estacion = "otoño"
    print("La estacion del mes es {}".format(estacion))
else:
    print("El mes no es valido")