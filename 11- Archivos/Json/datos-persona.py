import json

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

def readEdad():
    while True:
        try:
            num = int(input("Enter your age: "))
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

def readSexo():
    while True:
        try:
            phrase = input("Input gender: ")
            phrase = phrase.strip()
            if len(phrase) == 0 or phrase.isalnum() == False:
                print("Error: Invalid input, must be a string")
                input("Press any key to continue")
                print("\n", "=" * 30, "\n")
                continue
            elif phrase.lower() != "m" and phrase.lower() != "f":
                print("Gender must be either (M/F)")
                input("Press any key to continue")
                continue
            return phrase
        except Exception as e:
            print(f"Error: Invalid input, must be a string\n{e}")
            input("Press any key to continue")
            print("\n", "=" * 30, "\n")

def readTelefono():
    while True:
        try:
            num = int(input("Enter your phone number: "))
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
            phrase = input("Input the name of the Personal: ")
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

def guardarEmpleado(lstPersonal, ruta):
    try:
        fd = open(ruta, "w")
    except Exception as e:
        print("Error al abrir el archivo para guardar al empleado.\n", e)
        return None
    try:
        json.dump(lstPersonal, fd)
    except Exception as e:
        print("Error al guardar la informacion del emplaeado.\n")
        return None
    
    fd.close()
    return True

def existeId(id, lstPersonal):
    for datos in lstPersonal:
        k = int(list(datos.keys())[0])
        if k == id:
            return True
    return False

def borrarPersonal(lstPersonal, ruta):
    print("\n\n3. Borrar Personal")

    id = readId()
    if not existeId(id, lstPersonal):
        print("No existe un empleado cpn ese ID")
        input()
        return
    
    for i in range(len(lstPersonal)):
        datos = lstPersonal[i]
        k = int(list(datos.keys())[0])
        if k == id:
            del lstPersonal[i]
            break
    if guardarEmpleado(lstPersonal, ruta) == True:
        print("El empleado ha sido borrado con exito")
        input()
    else:
        print("Ocurrio un error al borrar el empleado")

def modifyPersonal(lstPersonal, ruta):
    id = readId()
    if existeId(str(id), lstPersonal):
        print("That ID does not exist")
        input()
        return
    while True:
            print("*** Modify Perosnal ***".center(40))
            print("1- Edit name")
            print("2- Edit age")
            print("3- Edit gender")
            print("4- Edit phone number")
            print("5- Return")
            n = int(input("Choose which option you would like to modify: "))
            if n < 1 or n > 5:
                print("Error: Input must be between 1 and 5")
                input("Press any key to continue")
                print("\n", "=" * 30, "\n")
                continue
            break
    if n == 1:
        for i in range(len(lstPersonal)):
            datos = lstPersonal[i]
            k = int(list(datos.keys())[0])
            if k == id:
                lstPersonal[i][str(id)]["nombre"] = readStr()
        if guardarEmpleado(lstPersonal, ruta) == True:
            print("The employee has been modified successfully")
            input()
        else:
            print("Ocurrio un error al borrar el empleado")

    elif n == 2:
        for i in range(len(lstPersonal)):
            datos = lstPersonal[i]
            
            k = int(list(datos.keys())[0])
            if k == id:
                
                lstPersonal[i][str(id)]["edad"] = readEdad()
        if guardarEmpleado(lstPersonal, ruta) == True:
            print("The employee has been modified successfully")
            input()
        else:
            print("Ocurrio un error al borrar el empleado")
    elif n == 3:
        for i in range(len(lstPersonal)):
            datos = lstPersonal[i]
            
            k = int(list(datos.keys())[0])
            if k == id:
                
                lstPersonal[i][str(id)]["sexo"] = readSexo()
        if guardarEmpleado(lstPersonal, ruta) == True:
            print("The employee has been modified successfully")
            input()
        else:
            print("Ocurrio un error al borrar el empleado")
    elif n == 4:
        for i in range(len(lstPersonal)):
            datos = lstPersonal[i]
            
            k = int(list(datos.keys())[0])
            if k == id:
                
                lstPersonal[i][str(id)]["telefono"] = readTelefono()
        if guardarEmpleado(lstPersonal, ruta) == True:
            print("The employee has been modified successfully")
            input()
        else:
            print("Ocurrio un error al borrar el empleado")



        

def agregarPersonal(lstPersonal, ruta):
    print("\n\n1. Agregar Personal")

    id = readId()
    while existeId(id , lstPersonal):
        print("==> Ya existe un empleado con ese ID")
        input()
        id = readId()

    nombre = readStr()
    edad = readEdad()
    sexo = readSexo()
    telefono = readTelefono()

    dicEmpleado = {}
    dicEmpleado[str(id)] = {"nombre":nombre, "edad":edad, "sexo":sexo, "telefono":telefono}
    lstPersonal.append(dicEmpleado)

    if guardarEmpleado(lstPersonal, ruta) == True:
        input("El empleado ha sido registrado con exito\nPresione cualquier tecla para contrinuar ... ")
    else:
        input("Ocurrio algun error al guardar el empleado.")

def menu():
    while True:
        try:
            print("\t*** REGISTRO DEL PERSONAL ***".center(40))
            print("MENU".center(40))
            print("1- Agregar")
            print("2- Modificar ")
            print("3- Eliminar ")
            print("4- Ver")
            print("5- Salir")
            opcion = int(input(">>>Ingrese una opcion: "))
            if opcion < 1 or opcion > 6:
                print("Error: Input must be between 1 and 8")
                input("Press any key to continue")
                print("\n", "=" * 30, "\n")
                continue
            return opcion
        except ValueError:
            print("Error: Invalid option")

def cargarInfo(lstPersonal, ruta):
    try:
        fd = open(ruta, "r")
    except Exception as e:
        try:
            fd = open(ruta, "w")
        except Exception as d:
            print("Error in trying to open archive\n", d)
            return None
    
    try:
        linea = fd.readline()
        if linea.strip() != "":
            fd.seek(0)
            lstPersonal = json.load(fd)
        else:
            lstPersonal = []
    except Exception as e:
        print("Error in loading information\n", e)
        return None
    
    print(lstPersonal)
    fd.close()
    return lstPersonal




# PROGRAMA PRINCIPAL
rutaFile = "11- Archivos/Json/datpersonal.json"
lstPersonal = []
lstPersonal = cargarInfo(lstPersonal, rutaFile)
while True:

    option = menu()
    if option == 1:
        agregarPersonal(lstPersonal, rutaFile)
        print(lstPersonal)
        pass
    elif option == 2:
        modifyPersonal(lstPersonal, rutaFile)
    elif option == 3:
        borrarPersonal(lstPersonal, rutaFile)
    elif option == 4:
        pass
    elif option == 5:
        break