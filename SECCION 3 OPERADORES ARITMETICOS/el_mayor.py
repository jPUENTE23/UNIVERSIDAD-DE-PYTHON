
num1 = int(input("Proporcione el numero 1: "))
num2 = int(input("Proporcione el numero 2: "))
comparacion1 = (num1 > num2)
comparacion2 = (num1 < num2)
comparacion3 = (num1 == num2)
if (comparacion1):
    print("El numero mayor es: {} ".format(num1))
else:
    if (comparacion2):
        print("El numero mayor es: {}".format(num2))
    else:
        if(comparacion3):
            print("Ambos numeros son iguales")