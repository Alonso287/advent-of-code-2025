def main():
    suma = 0
    with open(r"Día 3\entrada.txt") as entrada:
        baterías = entrada.readlines()
        for batería in baterías:
            suma += calcular_maximo(batería)
    print(suma)

def calcular_maximo(número):
    máximo = 0
    for n1 in range(len(número)):
        for n2 in número[n1 + 1:]:
            if int(número[n1] + n2) > máximo:
                máximo = int(número[n1] + n2)
    return máximo

if __name__ == "__main__":
    main()