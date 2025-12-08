with open(r"Día 7\entrada.txt") as entrada:
    mapa = entrada.readlines()

rayo_inicial = mapa[0].index("S")

rayos = [rayo_inicial]

def buscar_separadores(linea):
    indices = []
    for i in range(len(linea)):
        if linea[i] == "^":
            indices.append(i)
    return indices

suma = 0

for linea in mapa:
    for separador in buscar_separadores(linea):
        if separador in rayos:
            rayos.remove(separador)
            rayos.append(separador - 1)
            rayos.append(separador + 1)
            rayos = list(set(rayos))
            suma += 1

print(suma)