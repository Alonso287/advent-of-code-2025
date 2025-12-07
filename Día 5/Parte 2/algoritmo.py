with open(r"Día 5\rangos.txt") as rangos:
    rangos = rangos.readlines()
with open(r"Día 5\ids.txt") as ids:
    ids = ids.readlines()

rangos = [range(int(rango.split("-")[0]), int(rango.split("-")[1])+1) for rango in rangos]

