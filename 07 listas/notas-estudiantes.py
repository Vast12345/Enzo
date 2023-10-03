# Ejercicio
# Haacer un programa que lea N estrudiantes (nombre y nota). Y nos muestre el promedio de la clase, el estudiante con mayorr nota, el estudiante con menor nota
def readNum(str):
    while True:
        try:
            num = int(input(str))
            if num < 1:
                print("Error: Invalid input, must be a positive integer")
                input("Press any key to continue")
                print("\n", "=" * 30, "\n")
                continue
            return num
        except ValueError:
            print("Error: Invalid input, must be an integer")
            input("Press any key to continue")
            print("\n", "=" * 30, "\n")

def readStr(str):
    while True:
        try:
            phrase = (input(str))
            phrase = phrase.strip()
            if len(phrase) == 0 or phrase.isalnum() == False:
                print("Error: Invalid input, must be a string")
                input("Press any key to continue")
                print("\n", "=" * 30, "\n")
                continue
            return phrase
        except Exception as e:
            print(f"Error: Invalid input, must be a string\n{e}")
            input("Press any key to continue")
            print("\n", "=" * 30, "\n")

def readNota(str):
    while True:
        try:
            num = float(input(str))
            if num < 0:
                print("Error: Invalid input, must be a more than zero.")
                input("Press any key to continue")
                print("\n", "=" * 30, "\n")
                continue
            return num
        except ValueError:
            print("Error: Invalid input, must be an nota.")
            input("Press any key to continue")
            print("\n", "=" * 30, "\n")

n = readNum("Input the amount of users: ")
lstNombres = []
lstNota = []

for i in range(1, n+1):
    print("\nDatos del estudiante #", i)
    lstNombres.append(readStr("Nombre? "))
    lstNota.append(readNota("Nota? "))

# Calcular y mostrar el promedio 
prom = sum(lstNota) / n
print("\n", "=" * 30, "\n")
print(f"El promedio del curso es: {prom:.1f}")

# Encontrar y mostrar el estudiante con mayor nota
notaMayor = max(lstNota)
posEstMayor = lstNota.index(notaMayor)
nomEstMayorNota = lstNombres[posEstMayor]
print("El estudiante", nomEstMayorNota, " tiene la mayor nota:", notaMayor)

# Encotrar y mostrar el estudiante con menor nota
notaMenor = min(lstNota)
posEstMenor = lstNota.index(notaMenor)
nomEstMenorNota = lstNombres[posEstMenor]
print("El estudiante", nomEstMenorNota, " tiene la menor nota:", notaMenor)