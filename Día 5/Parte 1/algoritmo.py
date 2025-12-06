with open(r"Día 5\rangos.txt") as rangos:
    rangos = rangos.readlines()
with open(r"Día 5\ids.txt") as ids:
    ids = ids.readlines()

rangos = [range(int(rango.split("-")[0]), int(rango.split("-")[1])+1) for rango in rangos]

def comprobar_id(id):
    global rangos
    for rango in rangos:
        if id in rango:
            return True
    return False

suma  = 0

for id in range(len(ids)):
    print(f"{id+1} / 1000")
    if comprobar_id(int(ids[id])):
        suma += 1

print(suma)
