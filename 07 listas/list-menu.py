

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


lstId = []
lstName = []
lstHours = []
lstValue = []

def IndexID(id):
    index = lstName.index(id)
    return index

users = readNum("Input the amount of employees")
for i in range (users):
    try:
        print("\nDatos del empleado #", i+1)
        lstId.append(readNum("ID? "))
        lstName.append(readStr("Nombre? "))
        lstHours.append(readNum("Horas? "))
        if lstHours[i] < 1 or lstHours[i] > 160:
            print("Error: You could have only worked between 1 - 160 hours.")
            input("Press any key to continue")
            print("\n", "=" * 30, "\n")
            continue
        lstValue.append(readNum("Valor? "))
        if lstValue[i] < 8_000 or lstValue[i] > 150_000:
            print("Error: You could have only earned between $8,000 to 150,000 an hour.")
            input("Press any key to continue")
            print("\n", "=" * 30, "\n")
            continue
    except Exception as e:
        pass


while True:
    option = menu()
    if option == 1:
        print("* New Employee *")
        lstId.append(readNum("ID? "))
        lstName.append(readStr("Nombre? "))
        lstHours.append(readNum("Horas? "))
        if lstHours[-1] < 1 or lstHours[-1] > 160:
            print("Error: You could have only worked between 1 - 160 hours.")
            input("Press any key to continue")
            print("\n", "=" * 30, "\n")
        lstValue.append(readNum("Valor? "))
        if lstValue[-1] < 8_000 or lstValue[-1] > 150_000:
            print("Error: You could have only earned between $8,000 to 150,000 an hour.")
            input("Press any key to continue")
            print("\n", "=" * 30, "\n")
    elif option == 2:
        id = readNum("Input the user using his/her ID number to modify: ")
        index = IndexID(id)

        lstName.pop(index)
        lstHours.pop(index)
        lstValue.pop(index)
        lstName.insert(index, readStr("Nuevo Nombre? "))
        lstHours.insert(index, readNum("Nuevo Horas? "))
        if lstHours < 1 or lstHours > 160:
            print("Error: You could have only worked between 1 - 160 hours.")
            input("Press any key to continue")
            print("\n", "=" * 30, "\n")
        lstValue.insert(index, readNum("Nuevo Valor? "))
        if lstValue < 8_000 or lstValue > 150_000:
            print("Error: You could have only earned between $8,000 to 150,000 an hour.")
            input("Press any key to continue")
            print("\n", "=" * 30, "\n")
    elif option == 3:
        id = readNum("Input the user using his/her ID number to search: ")
        index = IndexID(id)
        searchName = lstName.index(index)
        searchHours = lstHours.index(index)
        searchValue = lstValue.index(index)
        print("\n", "=" * 30, "\n")
        print(f"The Name of the identifier is {searchName}, the hours they work are {searchHours}, and the value they earn is {searchValue}")
    elif option == 4:
        id = readNum("Input the user using his/her ID number to delete: ")
        index = IndexID(id)
        lstId.pop(index)
        lstName.pop(index)
        lstHours.pop(index)
        lstValue.pop(index)
        print("\n", "=" * 30, "\n")
    elif option == 5:
        print("\n", "=" * 30, "\n")
        continuemore = 0
        for i in range(i, continuemore + 5): 
            try:
                print(f"ID: {lstId[i]}, Name: {lstName[i]}, Hours: {lstHours[i]}, Value: {lstValue[i]}")
                if range(len(lstId)) > 5:
                         
                    move = readStr("Would you like to continue: Y/N ")

                    if move.lower() == "y":
                        continuemore += 5
                        continue
                    elif move.lower() == "n":
                        break
                    else:
                        print("Error: Invalid input, must be Y or N")
            except IndexError as e:
                print(f"Error: {e}")
            



