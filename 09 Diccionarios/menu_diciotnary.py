
# Function that reads the ID 
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

# Function specifically to delete the ID, only difference from the previous function is the change in print
def deleteId():
    while True:
        try:
            num = int(input("Input the ID you wish to erase: "))
            if num < 1:
                print("Error, ID must be a positive integer")
                input("Press any key to continue")
                print("\n", "=" * 30, "\n")
                continue
            return num
        except ValueError:
            print("Error: ID must be an integer")
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

def searchEmployee(dicEmployee, ID):
    employee = findEmployee(dicEmployee, ID)
    if employee is not None:
        print(f"Name: {dicEmployee[ID]['name']}")
        print(f"Hours: {dicEmployee[ID]['hours']}")
        print(f"Value per hour: {dicEmployee[ID]['value_per_hour']}")
        print(f"Salary: {dicEmployee[ID]['salary']:,.2f}")
        input()
    else:
        print("That Employee does not exist")
        input()
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
    datEmployee["value_per_hour"] = readVal()
    datEmployee["salary"] = datEmployee["value_per_hour"] * datEmployee["hours"]

    dicEmployee[id] = datEmployee

def modifyEmployee(dicEmployee, ID):
    if findEmployee(dicEmployee, ID) == None:
        print("The ID already exist")
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
        dicEmployee[ID]["name"] = readStr()
    elif n == 2:
        dicEmployee[ID]["hours"] = readHours()
    elif n == 3:
        dicEmployee[ID]["value_per_hour"] = readVal()

    dicEmployee[ID]["salary"] = dicEmployee[ID]["hours"] * dicEmployee[ID]["value_per_hour"]
    input()
    
def eraseEmployee(dicEmployee, ID):
        if findEmployee(dicEmployee, ID) == None:
            print("That ID does not exist, try again.")
            input()
            return
        op = input("\nAre you sure you wish to erase this employee(Y/N)? ")
        if op.lower() == "y":
            dicEmployees.pop(ID)

def listEmployees(lstEmployees):
    count = 0
    # The for loop will go through every key inside of lstEmployees, and then the values within that key
    for k, v in lstEmployees.items():
        print("\n", "=" * 30, "\n")
        print(f"ID: {k}")
        print(f"Name: {v['name']}")
        print(f"Hours: {v['hours']}")
        print(f"Value per hour: {lstEmployees[k]['value_per_hour']}")
        print(f"Salary: {lstEmployees[k]['salary']}")
        print("\n", "=" * 30, "\n")
        
        count += 1

        if count % 5 == 0:
            op = input("Do you wish to continue? (Y/N) ")
            if op.lower() == "n":
                return

def lstNomina(dicEmployee, ID):
    if findEmployee(dicEmployee, ID) == None:
        print("That ID does not exist.")
        input()
        return
    
    sal = dicEmployee[ID]["salary"]
    if sal < 1_600_000:
        aux_trans = 140_000
    else:
        aux_trans = 0
    eps = 0.04 * sal
    pen = 0.04 * sal

    net_sal = sal + aux_trans - eps - pen
    print("\n", "=" * 30, "\n")
    print(f"Salary: ${sal:,}\nGross salary: ${net_sal:,.2f}")

def lstNomEmployees(lstEmployees):
    count = 0
    # The for loop will go through every key inside of lstEmployees, and then the values within that key
    for k, v in lstEmployees.items():
        sal = lstEmployees[k]["salary"]
        if sal < 1_600_000:
            aux_trans = 140_000
        else:
            aux_trans = 0
        eps = 0.04 * sal
        pen = 0.04 * sal
        net_sal = sal + aux_trans - eps - pen

        print("\n", "=" * 30, "\n")
        print(f"Salary of {v['name']}: ${sal:,}\nGross salary of {v['name']}: ${net_sal:,.2f}")
            
        count += 1

        if count % 5 == 0:
            op = input("Do you wish to continue? (Y/N) ")
            if op.lower() == "n":
                return


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
        addEmployee(dicEmployees)
        print(dicEmployees)
        input()
    elif option == 2:
        modifyEmployee(dicEmployees, readId())
        print(dicEmployees)
        input()
    elif option == 3:
        print(searchEmployee(dicEmployees, readId()))
    elif option == 4:
        eraseEmployee(dicEmployees, readId())
        print(dicEmployees)
        input()
        pass
    elif option == 5:
        listEmployees(dicEmployees)
        input()
    elif option == 6:
        lstNomina(dicEmployees, readId())
        input()
    elif option == 7:
        lstNomEmployees(dicEmployees)
        input()
    elif option == 8:
        input()
        break
        


