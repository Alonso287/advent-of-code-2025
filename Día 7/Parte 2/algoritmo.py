with open(r"Día 7\entrada.txt") as entrada:
    mapa = entrada.readlines()

rayo_inicial = mapa[0].index("S")

rayos = [1 if c == "S" else 0 for c in list(mapa)[0]]

def buscar_separadores(linea):
    indices = []
    for i in range(len(linea)):
        if linea[i] == "^":
            indices.append(i)
    return indices

mapa = [linea for linea in mapa if buscar_separadores(linea) != []]

total = 0
for linea in mapa:
    for separador in buscar_separadores(linea):
        rayos[separador - 1] += rayos[separador]
        rayos[separador + 1] += rayos[separador]
        rayos[separador] = 0
        total = sum(rayos)

print(total)