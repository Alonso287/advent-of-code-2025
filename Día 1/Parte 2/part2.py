def part2(posicion=0, pasos=0):

    if pasos >= 0:
        return abs(pasos + posicion) // 100

    contraseña = abs(pasos) // 100

    pasos = - (abs(pasos) % 100)

    if (posicion + pasos) <= 0 and posicion != 0:
        return contraseña + 1

    return contraseña


def main():
    main()

if __name__ == "__main__":
    main()