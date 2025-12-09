with open(r"Día 9\entrada.txt") as entrada:
    entrada = entrada.readlines()

puntos = [[int(linea.split(",")[0]), int(linea.split(",")[1])] for linea in entrada]

def calcular_area(punto1, punto2):
    return (abs(punto2[0] - punto1[0])+1) * (abs(punto2[1] - punto1[1])+1)

max = 0
for i in puntos:
    for j in puntos:
        if calcular_area(i,j) > max:
            max = calcular_area(i,j)
            p1 = i
            p2 = j

print(max, p1, p2)
