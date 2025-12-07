import re

with open(r"Día 6\entrada.txt") as numeros:
    numeros = numeros.readlines()

operadores = numeros.pop(4)

operadores = re.split(r" +", operadores.strip())

numeros = [re.split(r" +", linea.strip()) for linea in numeros]
numeros = [[int(n) for n in linea] for linea in numeros]

total = 0

for i in range(1000):
    if operadores[i] == "*":
        total += numeros[0][i] * numeros[1][i] * numeros[2][i] * numeros[3][i]
    if operadores[i] == "+":
        total += numeros[0][i] + numeros[1][i] + numeros[2][i] + numeros[3][i]

print(total)
