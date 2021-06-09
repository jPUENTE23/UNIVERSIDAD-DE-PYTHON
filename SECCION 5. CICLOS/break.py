# imprimir solo letras a
# deacuerdo a cuentas letras a tenga la siguiente palabra
# nos lo mostrara en pantalla
for letra in "Alemania":
    if letra == "a":
        print(letra)

# pero si interrumpimos con un break solo nos mmostarar la primera "a" de la palabra

for letra in "Alemania":
    if letra == "a":
        print(letra)
        break

# continue
for i in range (10):
    if i%3 != 0:
        continue
    print(i)