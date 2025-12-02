def calcular_veces_por_0(posicion, pasos):

    if pasos >= 0:
        return abs(pasos + posicion) // 100

    contraseña = abs(pasos) // 100

    pasos = - (abs(pasos) % 100)

    if (posicion + pasos) <= 0 and posicion != 0:
        return contraseña + 1

    return contraseña