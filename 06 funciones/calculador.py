def suma(num1, num2):
    result = num1 + num2
    return result

def resta(num1, num2):
    return num1 - num2

def multiplic(num1, num2):
    return num1 * num2

def division(num1, num2):
    try:
        result = num1 / num2
    except ZeroDivisionError:
        result = None
    return result
    

def menu():
    while True:
        try:
            print("*** CALCULATOR MENU ***")
            print("1. Sumar")
            print("2. Restar")
            print("3. Multiplicar")
            print("4. Dividir")
            print("5. Salir")
            option = int(input(">>> Option (1-5)? "))
            if option < 1 or option > 5:
                print("Invalid option. Choose from the following.")
                input("Presione cualquire tecla para continuar ... ")
                continue
            return option
        except ValueError:
            print("Invalid option. Choose from the following.")
            input("Presione cualquire tecla para continuar ... ")
    
def leerNum(mensaje):
    while True:
        try:
            num = float(input(mensaje))
            return num
        except ValueError:
            print("Error, invalid number.")
            input("Presione cualquier tecla para continuar... ")


## PROGRAMA PRINCIPAL
while True:
    opcion = menu()
    
    if opcion == 1:
        print("\n\n1. SUMAR")
        num1 = leerNum("Ingrese el primer numero: ")
        num2 = leerNum("Ingrese el segundo numero: ")
        print(f"El resultado de la suma es: {suma(num1, num2):,.3f}")
    elif opcion == 2:
        print("\n\n2. RESTAR")
        num1 = leerNum("Ingrese el primer numero: ")
        num2 = leerNum("Ingrese el segundo numero: ")
        print(f"El resultado de la resta es: {resta(num1, num2):,.3f}")
    elif opcion == 3:
        print("\n\n3. MULTIPLICAR")
        num1 = leerNum("Ingrese el primer numero: ")
        num2 = leerNum("Ingrese el segundo numero: ")
        print(f"El resultado de la multiplicacion es: {multiplic(num1, num2):,.3f}")
    elif opcion == 4:
        print("\n\n4. DIVIDIR")
        num1 = leerNum("Ingrese el primer numero: ")
        num2 = leerNum("Ingrese el segundo numero: ")
        res = division(num1, num2)
        if res != None:
            print(f"El resultado de la division es: {res:,.3f}")
        else:
            print("No se puede dividir por cero")
    elif opcion == 5:
        print("\n\nGracias por usar la calculadora ")
        print("Adios")
        input("Presione cualquier tecla para salir ... ")
        break
    input("Presione cualquier tecla para volver al MENU ... ")

                
    