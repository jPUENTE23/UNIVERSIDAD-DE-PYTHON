
# sentencia if ordinaria
numero = int(input("Ingrea un numero entre 1 y 3: "))

# empesamos a validar de acuerdo al numero ingresado
if (numero == 1):
    numeroEnTxt = "Numero uno"
else:
    if (numero == 2):
        numeroEnTxt = "Numero dos"
    else:
        if (numero == 3):
            numeroEnTxt = "Numero tres"
        else:
            # si se ingreso un numero que no se encuentra dentro de la sentencia
            # el else hara que manda un mensaje
            print("Ingreso un numero no valido")

print("El numero en texto es {}".format(numeroEnTxt))


# sentencia elif

numero2 = int(input("Ingresa un numero entre 4 y 6: "))

if (numero2 == 4):
    numeroEnTxt_ = "Numero cuatro"
elif (numero2 == 5):
    numeroEnTxt_ = "Numero cinco"
elif (numero2 == 6):
    numeroEnTxt_ = "Numero seis"
else:
    print("Ingreso un numero no valido")

print("El numero en texto es {}".format(numeroEnTxt_))