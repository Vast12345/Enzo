import json

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

    id = int(input("Input ID: "))
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

def agregarPersonal(lstPersonal, ruta):
    print("\n\n1. Agregar Personal")

    id = int(input("Input the ID: "))
    while existeId(id , lstPersonal):
        print("==> Ya existe un empleado con ese ID")
        input()
        id = int(input("\nInput the ID: "))

    nombre = input("Name: ")
    edad = int(input("Age: "))
    sexo = input("Sexo (M/F): ")
    telefono = int(input("Telefono: "))

    dicEmpleado = {}
    dicEmpleado[id] = {"nombre":nombre, "edad":edad, "sexo":sexo, "telefono":telefono}
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
        pass
    elif option == 2:
        pass
    elif option == 3:
        borrarPersonal(lstPersonal, rutaFile)
    elif option == 4:
        pass
    elif option == 5:
        break