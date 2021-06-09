

numeros = (13, 1, 8, 3, 2, 5, 8)
menoresA5 = list()

for num in numeros:
    # si durante el ciclo for, num encuentra un valor que sea menos a 5
    # lo guardara en la lista menosresA5
    if num < 5:
        menoresA5.append(num)

print("Los numeros menores a 5 encontrados en la tupla son {} ".format(menoresA5))