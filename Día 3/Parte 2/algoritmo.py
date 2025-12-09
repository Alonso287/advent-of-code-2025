numero = 811111111111119
numero = str(numero)

max = ""
digito_max = -1

while len(max) != 12:

    numero2 = numero[digito_max+1:-(11-len(max))]

    if len(numero2) + len(max) == 12:
        max = max + numero2
        break

    # Lista de los dígitos que se pueden escoger, de menor a mayor
    digitos_ordenados = numero2
    digitos_ordenados = list(digitos_ordenados)
    digitos_ordenados = [int(n) for n in digitos_ordenados]
    digitos_ordenados = sorted(digitos_ordenados)
    digitos_ordenados.reverse()
    digitos_ordenados = [str(n) for n in digitos_ordenados]

    print(numero2)
    print(digitos_ordenados)

    # Busca el mayor número posible que se pueda escoger, lo más cerca posible del inicio de la cadena
    digito_max = numero.index(digitos_ordenados[0])

    print(numero[digito_max])

    #añade al número definitivo el dígito que hemos encontrado
    max = max + numero[digito_max]

print(max)