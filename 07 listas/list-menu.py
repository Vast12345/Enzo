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

def agregarEmpleados(lstEmpleados):
    print("* New Employee *")
    lstDatos = []
    lstDatos.append(readNum())
    lstDatos.append(readStr())
    lstDatos.append(readHours())
    lstDatos.append(readVal())

    lstEmpleados.append(lstDatos)

def Modify(lstEmpleados):





while True:
    option = menu()
    lstEmpleados = []
    if option == 1:
        print("* New Employee *")
        agregarEmpleados(lstEmpleados)
        print(lstEmpleados)
        input()
    elif option == 2:
        Modify()
        




