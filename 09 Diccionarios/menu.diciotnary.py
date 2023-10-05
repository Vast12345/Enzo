

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

def findEmployee(dicEmployee, ID):
    for k, v in dicEmployee.items():
        if k == ID:
            return k
    return None

def addEmployee(dicEmployee):
    print("*** New Employee***")
    datEmployee = {}
    id = readId()
    if findEmployee(dicEmployee, id) != None:
        print("The ID already exists.")
        input()
        return
    datEmployee["name"] = readStr()
    datEmployee["hours"] = readHours()
    datEmployee["value"] = readVal()

    dicEmployee[id] = datEmployee

def modifyEmployee(dicEmployee, ID):
    if findEmployee(dicEmployee, ID) == None:
        print("The ID already exist")
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


dicEmployees = {}
while True:
    option = menu()
    if option == 1:
        addEmployee()
        print(addEmployee)
        input()
    elif option == 2:

