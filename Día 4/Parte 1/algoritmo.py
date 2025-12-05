with open(r"Día 4\entrada.txt") as datos:
    datos = datos.readlines()
    datos = [dato.strip() for dato in datos]
    datos = [[1 if dato == "@" else 0 for dato in linea] for linea in datos]

suma = 0

datos2 = datos.copy()

for fila in range(len(datos)):
    limite = len(datos[fila]) - 1
    for columna in range(len(datos[fila])):
        alrededores = 0

        if fila != 0:
            if columna != 0:
                alrededores += datos[fila-1][columna - 1]   # Arriba-Izquierda

            alrededores += datos[fila-1][columna]           # Arriba-Centro

            if columna != limite:
                alrededores += datos[fila-1][columna + 1]   # Arriba-Derecha

        if columna != 0:
            alrededores += datos[fila][columna - 1]         # Centro-Izquierda

        if columna != limite:
            alrededores += datos[fila][columna + 1]         # Centro-Derecha

        if fila != limite:
            if columna != 0:
                alrededores += datos[fila+1][columna - 1]   # Abajo-Izquierda

            alrededores += datos[fila+1][columna]           # Abajo-Centro

            if columna != limite:
                alrededores += datos[fila+1][columna + 1]   # Abajo-Derecha
        
        if alrededores < 4 and datos[fila][columna] == 1:
            suma += 1

print(suma)