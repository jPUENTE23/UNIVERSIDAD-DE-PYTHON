
numeros = list()

for num in range (10):
    numeros.append(num)
    if num%3:
        continue
    print(num)