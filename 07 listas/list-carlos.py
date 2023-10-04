def leerValHoraEmpl():
    while True:
        try:
            num = int(input("Ingrese el valor de la hora trabajaba del empleado: "))
            if num < 8_000 or num > 150_000:
                print("Valor de la Hora invalida, debe ser en range de [8000, 150000]")
                input("Press any key to continue")
                print("\n", "=" * 30, "\n")
                continue
            return num
        except ValueError:
            print("Error: Invalid input, must be an integer")
            input("Press any key to continue")
            print("\n", "=" * 30, "\n")

def leerIDEmpl():
    while True:
        try:
            num = int(input("Ingrese el ID del empleado: "))
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

def leerHoraTrabEmpl():
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

def leerNombreEmpl():
    while True:
        try:
            phrase = (input("Ingrese el Nombre del empleado: "))
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

def buscarEmpleado(lstEmpleado, idEmpl):
    for i in range(len(lstEmpleado)):
        if (lstEmpleado[i][0] == idEmpl):
            return i
    return -1

def modificarEmpleado(lstEmpleado):
    print("2. Modificar Empleado\n")

    idEmpl = leerIDEmpl()
    posEmpl = buscarEmpleado(lstEmpleado, idEmpl)
    if posEmpl == -1:
        print("El codigo del empleado no existe.")
        input()
        return
    print("\n")
    while True:
        op = int(input("\n1. Nombre\n2. Cantidad de Horas\n3. Valor de la hora\nOpcion? "))
        if op < 1 or op > 3:
            print("Opcion invalida")
            input()
            continue
        break
    if op == 1:
        nombre = leerNombreEmpl()
        lstEmpleado[posEmpl][1] = nombre
    elif op == 2:
        cantHoras = leerHoraTrabEmpl()
        lstEmpleado[posEmpl][1] = cantHoras
    elif op == 3:
        valHoras = leerValHoraEmpl()
        lstEmpleado[posEmpl][1] = valHoras


def agregarEmpleado(lstEmpleado):
    print("\n\n*** 1. Agregar empleado\n")
    lstDatos = []
    id = leerIDEmpl()
    if buscarEmpleado(lstEmpleado, id) != -1:
        print("El id ya existe en la lista")
        input()
        return
    lstDatos.append(leerIDEmpl())
    lstDatos.append(leerNombreEmpl())
    lstDatos.append(leerHoraTrabEmpl())
    lstDatos.append(leerValHoraEmpl())

    lstEmpleado.append(lstDatos)

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

lstEmpleado = []
while True:
    op = menu()
    if op == 1:
        agregarEmpleado(lstEmpleado)
        print(lstEmpleado)
        input()
    elif op == 2:
        pass
        
    elif op == 3:
        pass
    elif op == 4:
        pass
    elif op == 5:
        pass
    elif op == 6:
        pass
    elif op == 7:
        pass
    elif op == 8:
        break