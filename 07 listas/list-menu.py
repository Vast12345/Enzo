def readId():
    while True:
        try:
            num = int(input("Enter your ID: "))
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

def readStr():
    while True:
        try:
            phrase = input("Input the name of the employee: ")
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



def readHours():
    while True:
        try:
            num = int(input("Ingrese las horas trabajabas del empleado: "))
            if num < 1 or num > 160:
                print("Error: Invalid input, must in the range of [1, 160]")
                input("Press any key to continue")
                print("\n", "=" * 30, "\n")
                continue
            return num
        except ValueError:
            print("Error: Invalid input, must be an integer")
            input("Press any key to continue")
            print("\n", "=" * 30, "\n")

def readVal():
    while True:
        try:
            num = int(input("Ingrese el valor de la hora del empleado: "))
            if num < 8_000 or num > 150_000:
                print("Error: Invalid input, must be bewtween 8000 to 150000")
                input("Press any key to continue")
                print("\n", "=" * 30, "\n")
                continue
            return num
        except ValueError:
            print("Error: Invalid input, must be an integer")
            input("Press any key to continue")
            print("\n", "=" * 30, "\n")


def findEmployee(lstEmployees, ID):
    for i in range(len(lstEmployees)):
        if lstEmployees[i][0] == ID:
            return i
    return -1
    
def Modify(lstEmpleados, ID):
    posID = findEmployee(lstEmpleados, ID)
    if posID == -1:
        print("El id no existe en la lista")
        input()
        return
    while True:
        print("* Modify Employee *")
        print("1- Change name")
        print("2- Change hours")
        print("3- Change value from hours")
        n = int(input("Choose which option you would like to modify: "))
        if n < 1 or n > 3:
            print("Error: Input must be between 1 and 3")
            input("Press any key to continue")
            print("\n", "=" * 30, "\n")
            continue
        break
    if n == 1:
        name = readStr()
        lstEmpleados[posID][1] = name
    elif n == 2:
        hours = readHours()
        lstEmpleados[posID][2] = hours
    elif n == 3:
        val = readVal()
        lstEmpleados[posID][3] = val

# def deleteEmployee(lstEmpleados, ID):


def agregarEmpleados(lstEmpleados):
    print("* New Employee *")
    id = readId()
    if findEmployee(lstEmpleados, id) != -1:
        print("The ID already exists.")
        input()
        return
    lstDatos = []
    lstDatos.append(id)
    lstDatos.append(readStr())
    lstDatos.append(readHours())
    lstDatos.append(readVal())

    lstEmpleados.append(lstDatos)


def menu():
    while True:
        try:
            print("*** MENU ***")
            print("1- Agregar empleado")
            print("2- Modificar empleado")
            print("3- Buscar empleado")
            print("4- Eliminar empleado")
            print("5- Listar empleados")
            print("6- Listar nomina de empleados")
            print("7- Listar nomina de todos los empleados")
            print("8- Salir")
            opcion = int(input("Ingrese una opcion: "))
            if opcion < 1 or opcion > 8:
                print("Error: Input must be between 1 and 8")
                input("Press any key to continue")
                print("\n", "=" * 30, "\n")
                continue
            return opcion
        except ValueError:
            print("Error: Invalid option")


lstEmpleados = []
while True:
    option = menu()
    if option == 1:
        agregarEmpleados(lstEmpleados)
        print(lstEmpleados)
        input()
    elif option == 2:
        Modify(lstEmpleados, readId())
        print(lstEmpleados)
        input()
    elif option == 3:
        posID = findEmployee(lstEmpleados, readId())
        print(lstEmpleados[posID])
        input()
    elif option == 4:
        pass
    elif option == 5:
        pass
    elif option == 6:
        pass
    elif option == 7:
        pass
    elif option == 8:
        input()
        break

        




