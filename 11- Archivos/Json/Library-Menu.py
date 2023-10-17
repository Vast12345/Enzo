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
            print("MENU".center(40))
            print("1- INSERT")
            print("2- CONSULTA ")
            print("3- EXIT")
            opcion = int(input(">>>Ingrese una opcion: "))
            if opcion < 1 or opcion > 3:
                print("Error: Input must be between 1 and 3")
                input("Press any key to continue")
                print("\n", "=" * 30, "\n")
                continue
            return opcion
        except ValueError:
            print("Error: Invalid option")

def existId(code, listLibrary):
    for data in listLibrary:
        k = int(list(data.keys())[0])
        if k == code:
            return True
    return False

def saveLibrary(lstLibrary, route):
    try:
        fd = open(route, "w")
    except Exception as e:
        print("Error in opening archive to save library.\n", e)
        return None
    try:
        LstLibrary = sorted(lstLibrary, key=lambda x: list(x.keys())[0], reverse=True)
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


routeFile = "/home/Exegol-161/Enzo/11- Archivos/Json/LIbrary-Archive.json"
lstLibrary = []
lstLibrary = loadInfo(lstLibrary, routeFile)

while True:
    option = menu()
    if option == 1:
        addRegister(lstLibrary, routeFile)
        pass
    elif option == 2:
        consultRegister(lstLibrary, routeFile)
        pass
    elif option == 3:
        break
    
