import re
from tkinter import VERTICAL

with open(r"Día 6\entrada.txt") as numeros:
    numeros = numeros.readlines()

operadores = numeros.pop(4)

operadores = re.findall(r"[*\+] *", operadores)

suma = 0

while len(operadores) != 0:
    # Obtener los 4 dígitos de la columna correspondiente
    num1 = numeros[0][:len(operadores[0])]
    num2 = numeros[1][:len(operadores[0])]
    num3 = numeros[2][:len(operadores[0])]
    num4 = numeros[3][:len(operadores[0])]

    # Obtener los números correspondientes de cada columna
    num1_vertical = num1[0] + num2[0] + num3[0] + num4[0]
    num2_vertical = num1[1] + num2[1] + num3[1] + num4[1]
    if len(operadores[0])-1 >= 3:
        num3_vertical = num1[2] + num2[2] + num3[2] + num4[2]
    if len(operadores[0])-1 >= 4:
        num4_vertical = num1[3] + num2[3] + num3[3] + num4[3]

    # Convierte cada número a int
    num1_vertical = int(num1_vertical)
    num2_vertical = int(num2_vertical)
    if len(operadores[0])-1 >= 3:
        num3_vertical = int(num3_vertical)
    if len(operadores[0])-1 >= 4:
        num4_vertical = int(num4_vertical)

    # Operar los números
    if operadores[0].strip() == "*":
        resultado = num1_vertical * num2_vertical
        if len(operadores[0])-1 >= 3:
            resultado *= num3_vertical
        if len(operadores[0])-1 >= 4:
            resultado *= num4_vertical
        suma += resultado
    elif operadores[0].strip() == "+":
        resultado = num1_vertical + num2_vertical
        if len(operadores[0])-1 >= 3:
            resultado += num3_vertical
        if len(operadores[0])-1 >= 4:
            resultado += num4_vertical
        suma += resultado

    # Eliminar cada número de la entrada
    numeros[0] = numeros[0].replace(num1, "", 1)
    numeros[1] = numeros[1].replace(num2, "", 1)
    numeros[2] = numeros[2].replace(num3, "", 1)
    numeros[3] = numeros[3].replace(num4, "", 1)

    # Elimina el primer operador de la lista
    operadores.pop(0)

print(suma)
