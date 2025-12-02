"""
ADVENT OF CODE - DÍA 1 - PARTE 2
--------------------------------------------------------------------------------
EXPLICACIÓN DETALLADA EN https://adventofcode.com/2025/day/1#part2
--------------------------------------------------------------------------------
Adicionalmente, al algoritmo anterior tenemos que añadir que hay que calcular
cada vez que el dial pase por la posición 0, aunque no se detenga allí.
"""

def main():
    posicion = 50                                               # Estado inicial del dial
    contraseña = 0
    with open(r"Día 1\Parte 1\entrada.txt", "r") as entrada:    # Abre el archivo con las instrucciones
        instrucciones = entrada.readlines()                     # Carga todas las líneas de entrada.txt
        for instruccion in instrucciones:
            pasos = calcular_pasos(instruccion)

            contraseña += calcular_veces_por_0(posicion, pasos)

            posicion += pasos
            posicion = posicion % 100
    print(contraseña)


def calcular_pasos(paso):
    """Interpreta la instrucción y devuelve el número de pasos correcto."""
    direccion = paso[0]
    pasos = int(paso[1:])
    return pasos if direccion == "R" else - pasos

def calcular_veces_por_0(posicion, pasos):
    """Calcula las veces que el dial pasa por el punto 0"""

    if pasos >= 0:
        return abs(pasos + posicion) // 100

    contraseña = abs(pasos) // 100

    pasos = - (abs(pasos) % 100)

    if (posicion + pasos) <= 0 and posicion != 0:
        return contraseña + 1

    return contraseña


if __name__ == "__main__":
    main()