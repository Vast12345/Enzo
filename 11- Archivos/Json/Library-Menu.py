import json

def readCode():
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

def readTitle():
    while True:
        try:
            phrase = input("Input Title: ")
            phrase = phrase.strip()
            if len(phrase) == 0 or phrase.isdigit() == True:
                print("Error: Invalid input, must be a string")
                input("Press any key to continue")
                print("\n", "=" * 30, "\n")
                continue
            return phrase
        except Exception as e:
            print(f"Error: Invalid input, must be a string\n{e}")
            input("Press any key to continue")
            print("\n", "=" * 30, "\n")

def readAuthor():
    while True:
        try:
            phrase = input("Input Author: ")
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

def readPrice():
    while True:
        try:
            num = int(input("Input Price: "))
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

def menu():
    while True:
        try:
            print("\t*** LIBRARY ***".center(40))
            print("MENU".center(45))
            print("1- INSERT")
            print("2- CONSULTA ")   
            print("3- EDIT")
            print("4- DELETE")
            print("5- LIST")
            print("6- EXIT")
            opcion = int(input(">>>Ingrese una opcion: "))
            if opcion < 1 or opcion > 6:
                print("Error: Input must be between 1 and 6")
                input("Press any key to continue")
                print("\n", "=" * 30, "\n")
                continue
            return opcion
        except ValueError:
            print("Error: Invalid option")

def editMenu():
    while True:
        print("*** Modify Book ***".center(45))
        print("1- Edit title")
        print("2- Edit author")
        print("3- Edit price")
        print("4- Return")
        n = int(input("Choose which option you would like to modify: "))
        if n < 1 or n > 4:
            print("Error: Input must be between 1 and 4")
            input("Press any key to continue")
            print("\n", "=" * 30, "\n")
            continue
        elif n == 4:
            break
        return n

def listMenu():
    while True:
        print("*** LIST LIBRARY***".center(45))
        print("1- List titles")
        print("2- List authors")
        print("3- List prices")
        print("4- Return")
        n = int(input("Choose which option you would like to modify: "))
        if n < 1 or n > 4:
            print("Error: Input must be between 1 and 4")
            input("Press any key to continue")
            print("\n", "=" * 30, "\n")
            continue
        elif n == 4:
            break
        return n

def existId(code, listLibrary):
    for data in listLibrary:
        k = int(list(data.keys())[0])
        if k == code:
            return True
    return False

def bubbleSortLibrary(lstLibrary):
    n = len(lstLibrary)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            # Compare the keys (book codes) of adjacent dictionaries
            key1 = list(lstLibrary[j].keys())[0]
            key2 = list(lstLibrary[j + 1].keys())[0]
            if key1 > key2:
                # Swap the dictionaries
                lstLibrary[j], lstLibrary[j + 1] = lstLibrary[j + 1], lstLibrary[j]

    return lstLibrary

def saveLibrary(lstLibrary, route):
    try:
        fd = open(route, "w")
    except Exception as e:
        print("Error in opening archive to save library.\n", e)
        return None
    try:
        #LstLibrary = sorted(lstLibrary, key=lambda x: list(x.keys())[0], reverse=True)
        lstLibrary = bubbleSortLibrary(lstLibrary)
        json.dump(LstLibrary, fd)
    except Exception as e:
        print("Error in saving the information of the new register.\n")
        return None

    fd.close()
    return True

def addRegister(lstLibrary, route):
    print("\n\n1. ADD REGISTER")

    code = readCode()
    while existId(code , lstLibrary):
        print("==> A book already exists with that ID")
        input()
        code = readCode()

    title = readTitle()
    author = readAuthor()
    price = readPrice()

    dicLibrary = {}
    dicLibrary[code] = {"title":title, "author":author, "price":price}
    lstLibrary.append(dicLibrary)

    if saveLibrary(lstLibrary, route) == True:
        input("The book has been registered successfully.\nPress any key to continue ... ")
    else:
        input("An error occurred while registering the book.")

def consultRegister(lstLibrary, route):
    code = readCode()
    if not existId(code, lstLibrary):
        print("That ID does not exist")
        print("\n", "=" * 30, "\n")
        input()
        return
    for i in range(len(lstLibrary)):
            datos = lstLibrary[i]
            k = int(list(datos.keys())[0])
            if k == code:
                print(f"\n")
                print(f"Title: {lstLibrary[i][str(code)]['title']}")
                print(f"\n")
                print(f"Author: {lstLibrary[i][str(code)]['author']}")
                print(f"\n")
                print(f"Price: {lstLibrary[i][str(code)]['price']}")
                print("\n", "=" * 30, "\n")
                break

def editRegister(lstLibrary, route):
    code = readCode()
    if existId(str(code), lstLibrary):
        print("That ID does not exist")
        input()
        return
    
    n = editMenu()
    if n == 1:
        for i in range(len(lstLibrary)):
            data = lstLibrary[i]
            k = int(list(data.keys())[0])
            if k == code:
                lstLibrary[i][str(code)]["title"] = readTitle()
        if saveLibrary(lstLibrary, route) == True:
            print("The employee has been modified successfully")
            input()
        else:
            print("Ocurrio un error al borrar el empleado")
    elif n == 2:
        for i in range(len(lstLibrary)):
            data = lstLibrary[i]
            
            k = int(list(data.keys())[0])
            if k == code:
                
                lstLibrary[i][str(code)]["author"] = readAuthor()
        if saveLibrary(lstLibrary, route) == True:
            print("The employee has been modified successfully")
            input()
        else:
            print("Ocurrio un error al borrar el empleado")
    elif n == 3:
        for i in range(len(lstLibrary)):
            data = lstLibrary[i]
            
            k = int(list(data.keys())[0])
            if k == code:
                
                lstLibrary[i][str(code)]["price"] = readPrice()
        if saveLibrary(lstLibrary, route) == True:
            print("The employee has been modified successfully")
            input()
        else:
            print("Ocurrio un error al borrar el empleado")

def eraseRegister(lstLibrary, route):
    print("\n\n3. Borrar Personal")

    code = readCode()
    if not existId(code, lstLibrary):
        print("No existe un empleado cpn ese ID")
        input()
        return
    
    for i in range(len(lstLibrary)):
        datos = lstLibrary[i]
        k = int(list(datos.keys())[0])
        if k == code:
            del lstLibrary[i]
            break
    if saveLibrary(lstLibrary, route) == True:
        print("El empleado ha sido borrado con exito")
        input()
    else:
        print("Ocurrio un error al borrar el empleado")

def listRegister(lstLibrary, route):
    
    n = listMenu()

    listTitle = []
    listAuthor = []
    listPrice = []
    for i in range(len(lstLibrary)):
        data = lstLibrary[i]
        listTitle.append(list(data.values())[0]['title'])
    for i in range(len(lstLibrary)):
        data = lstLibrary[i]
        listAuthor.append(list(data.values())[0]['author'])
    for i in range(len(lstLibrary)):
        data = lstLibrary[i]
        listPrice.append(list(data.values())[0]['price'])

    listTitle = sorted(listTitle)
    listAuthor = sorted(listAuthor)
    listPrice = sorted(listPrice)

    if n == 1:
        count = 0

        for e in listTitle:
            print("\n", "=" * 30, "\n")
            print(f"Title: {e}")
            print("\n", "=" * 30, "\n")
            
            count += 1

        if count % 3 == 0:
            op = input("Do you wish to continue? (Y/N) ")
            if op.lower() == "n":
                return
    elif n == 2:
        count = 0

        for e in listAuthor:
            print("\n", "=" * 30, "\n")
            print(f"Author: {e}")
            print("\n", "=" * 30, "\n")
            
            count += 1

        if count % 3 == 0:
            op = input("Do you wish to continue? (Y/N) ")
            if op.lower() == "n":
                return
    elif n == 3:
        count = 0

        for e in listPrice:
            print("\n", "=" * 30, "\n")
            print(f"Price: ${e}")
            print("\n", "=" * 30, "\n")
            
            count += 1

        if count % 3 == 0:
            op = input("Do you wish to continue? (Y/N) ")
            if op.lower() == "n":
                return

def loadInfo(lstLibrary, route):
    try:
        fd = open(route, "r")
    except Exception as e:
        try:
            fd = open(route, "w")
        except Exception as d:
            print("Error in trying to open archive\n", d)
            return None
    
    try:
        line = fd.readline()
        if line.strip() != "":
            fd.seek(0)
            lstLibrary = json.load(fd)
        else:
            lstLibrary = []
    except Exception as e:
        print("Error in loading information\n", e)
        return None
    
    print(lstLibrary)
    fd.close()
    return lstLibrary


routeFile = "/home/Exegol-161/Enzo/11- Archivos/Json/Library-Archive.json"
lstLibrary = []
lstLibrary = loadInfo(lstLibrary, routeFile)

while True:
    option = menu()
    if option == 1:
        addRegister(lstLibrary, routeFile)
    elif option == 2:
        consultRegister(lstLibrary, routeFile)
    elif option == 3:
        editRegister(lstLibrary, routeFile)
    elif option == 4:
        eraseRegister(lstLibrary, routeFile)
    elif option == 5:
        listRegister(lstLibrary, routeFile)
    elif option == 6:
        break
    
