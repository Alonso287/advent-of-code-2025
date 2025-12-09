from math import sqrt

import matplotlib.pyplot as plt
import numpy as np

def main():
    leer_datos()
    for caja in sorted(cajas, key=lambda caja:caja["distancia"]):
        print(caja["id"], caja["pareja"])
        print(caja["x"], cajas[caja["pareja"]]["x"])
        print()

def calcular_distancia(caja1, caja2):
    return sqrt((caja2["x"] - caja1["x"]) ** 2 + (caja2["y"] - caja1["y"]) ** 2 + (caja2["z"] - caja1["z"]) ** 2)

def calcular_caja_mas_cercana(id):
    distancias = []
    for i in range(len(cajas)):
        distancias.append(calcular_distancia(cajas[id], cajas[i]))

    distancias = [{"id":i, "distancia":distancias[i]} for i in range(len(distancias))]
    distancias = sorted(distancias, key=lambda caja:caja["distancia"])
    return distancias[1]["id"], distancias[1]["distancia"]

def calcular_duplicados():
    for caja in sorted(cajas, key=lambda cajas:cajas["id"]):
        pareja = cajas[caja["pareja"]]
        if caja["id"] == pareja["pareja"] and caja["pareja"] == pareja["id"] or caja["duplicado"] != None:
            caja["duplicado"] = True
            pareja["duplicado"] = False
        else:
            caja["duplicado"] = False

def leer_datos():
    print("Leyendo datos...")

    # Lee la entrada
    global cajas
    with open(r"Día 8\entrada.txt") as cajas:
        cajas = cajas.readlines()

    # Crea un diccionario con las coordenadas de cada caja
    cajas= [
        {"x":int(cajas[i].split(",")[0]), "y":int(cajas[i].split(",")[1]),"z":int(cajas[i].split(",")[2]), "id": i} 
        for i in range(len(cajas))]
    
    # Calcula la pareja de cada caja, es decir, la caja que tiene más cerca
    for i in range(len(cajas)):
        cajas[i]["pareja"] = calcular_caja_mas_cercana(i)[0]
        cajas[i]["distancia"] = calcular_caja_mas_cercana(i)[1]
        cajas[i]["duplicado"] = None

    calcular_duplicados()

    global parejas

    parejas = [caja for caja in cajas if caja["duplicado"] == False]

    print("Datos calculados")


if __name__ == "__main__":
    main()