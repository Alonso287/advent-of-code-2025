def main():
    suma = 0
    with open(r"Día 3\entrada.txt") as entrada:
        baterías = entrada.readlines()
        n = 0
        for batería in baterías:
            max = calcular_maximo(batería)
            suma += max
            n += 1
            print(len(str(max)))
            print(f"{n}/{len(baterías)}")
    print(suma)


def calcular_maximo(número):
    número = list(número)
    número_copia = número.copy()
    máximo = 0

    for i in range (len(número)):
        for j in range(len(número)-1):
            for k in range(len(número)-2):
                número_copia.pop(i)
                número_copia.pop(j)
                número_copia.pop(k)
                if int("".join(número_copia)) > máximo:
                    máximo = int("".join(número_copia))
                número_copia = número.copy()
    return máximo

número = 811111111111119

número = [int(n) for n in list(str(número))]

número_ordenado = número.copy()
número_ordenado = sorted(número_ordenado)
número_ordenado.reverse()



""" if __name__ == "__main__":
    main() """