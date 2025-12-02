def main():
    cuenta = 0
    with open(r"Día 2\entrada.txt") as entrada:
        rangos = entrada.readlines()[0].split(",")
        for rango in rangos:
            rango_menor, rango_mayor = [int(numero) for numero in rango.split("-")]
            for numero in range(rango_menor, rango_mayor+1):
                if es_un_patron(numero):
                     cuenta += numero
    print(cuenta)


def es_un_patron(numero):
    numero = str(numero)
    for digito in range(1,len(numero)+1):
        pieza_patron = numero[:digito]
        for repeticiones in range(2, len(numero) + 1):
            if numero == pieza_patron * repeticiones:
                return True
    return False

if __name__ == "__main__":
     main()