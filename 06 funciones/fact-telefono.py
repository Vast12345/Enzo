def calcularValorImpulso(impulso):
    return 100 * impulso

def calcularTarifaBasica(estrato):
    if estrato == 1:
        return 10000
    elif estrato == 2:
        return 15000
    elif estrato == 3:
        return 20000
    elif estrato == 4:
        return 25000
    elif estrato == 5:
        return 30000

def leerNombre(msj):
    while True:
        try:
            nom = (input(msj))
            nom = nom.strip()
            if len(nom) == 0 or nom.isalnum() == False:
                print("Valor invalido. Debe ser mayor a cero")
                continue
            return nom
        except Exception as e:
            print("Error.", e)
    
def leerEstrato(msj):
    while True:
        try:
            estrato = int(input(msj))
            if estrato < 1 or estrato > 5:
                print("Estrato invalido. Ingrese de 1 al 5")
                continue
            return estrato
        except ValueError:
            print("Error, ingrese un numero entero")

def leerInt(msj):
    while True:
        try:
            n = int(input(msj))
            if n < 1:
                print("Valor invalido. Debe ser mayor a cero")
                continue
            return n
        except ValueError:
            print("Error, ingrese un numero entero")


valtot = 0
n = leerInt("Ingrese la cantidad de usuarios: ")
for i in range(1, n+1):
    print("\nDatos del usuario #", i)
    name = leerNombre("Name: ")
    estrato = leerEstrato("Estrato: ")
    impulso = leerInt("Impulso: ")
    valtbas = calcularTarifaBasica(estrato)
    valimpu = calcularValorImpulso(impulso)
    
    print("=" * 30)
    print("Nombre:",name)
    print("Valor a pagar:", valtbas+valimpu)
    print("Tarifa basica:", valtbas)
    print("Valor de impulso:", valimpu)

    valtot += valtbas + valimpu
print("\n","*" * 30)
print(" El vsalor total a pagar es:",valtot)