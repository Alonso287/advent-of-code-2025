"""
ADVENT OF CODE - DÍA 1 - PARTE 1
--------------------------------------------------------------------------------
EXPLICACIÓN DETALLADA EN https://adventofcode.com/2025/day/1#part1
--------------------------------------------------------------------------------
El documento entrada.txt contiene las instrucciones para girar el dial.
El primer caracter indica la dirección, L=Izquierda y R=Derecha.
Los siguientes caracteres indican el número de veces que se tiene que girar el
dial en la dirección indicada.
El dial tiene 100 posiciones (0-99), así que hay que tener en cuenta cuando se
da la vuelta completa.
Además, para hallar la respuesta se tiene que contar las veces que el dial se
queda en la posición 0.
"""
def main():
    posicion = 50                                          # Estado inicial del dial
    contraseña = 0
    with open(r"Día 1\entrada.txt", "r") as entrada:    # Abre el archivo con las instrucciones
        instrucciones = entrada.readlines()             # Carga todas las líneas de entrada.txt
        for instruccion in instrucciones:
            posicion += calcular_pasos(instruccion)        # Calcula hacia dónde tiene que mover el dial
            posicion = posicion % 100                         # Se asegura de que el número esté entre 0 y 99
            if posicion == 0:                              # Si el dial está en la posición 0, se suma 1 a la contraseña
                contraseña += 1
    print(contraseña)


def calcular_pasos(paso):
    """Interpreta la instrucción y devuelve el número de pasos correcto."""
    direccion = paso[0]
    pasos = int(paso[1:])
    return pasos if direccion == "R" else - pasos


if __name__ == "__main__":
    main()