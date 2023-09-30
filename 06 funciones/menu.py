

def menu():
    while True:
        try:
            print("*** MENU ****")
            print("1- Factorial de un numero")
            print("2- Calcular Salario de un empleado")
            print("3- Calcular palabras en un parrafo")
            print("4- Salir")
            opcion = int(input("Ingrese una opcion (1-4): "))
            if opcion < 1 or opcion > 4:
                print("Invalid opcion: input must be between 1 and 4")
                input("Press any key to continue")
                continue
            return opcion
        except ValueError:
            print("Error: Invalid opcion, must be between 1 and 4")
            input("Press any key to continue")
def readNum(str):
    while True:
        try:
            num = int(input(str))
            if num < 0:
                print("Error: Invalid input, must be a positive integer")
                input("Press any key to continue")
                continue
            return num
        except ValueError:
            print("Error: Invalid input, must be an integer")
            input("Press any key to continue")

def readStr(str):
    while True:
        try:
            phrase = (input(str))
            phrase = phrase.strip()
            if len(phrase) == 0 or phrase.isalnum() == False:
                print("Error: Invalid input, must be a string")
                input("Press any key to continue")
                continue
            return phrase
        except Exception as e:
            print(f"Error: Invalid input, must be a string\n{e}")
            input("Press any key to continue")

def factorial(num):
    fact = 1
    for i in range(1, num+1):
        fact *= i
    return fact

def salarioEmpleado(hours, salary):
    extra_hours = 0
    for i in range(1, hours+1):
        if i > 40:
            extra_hours += 1
    totalEarn = (hours - extra_hours) * salary
    if hours > 40:
        extraSalary = salary * 1.5
        overtime = extra_hours * extraSalary
        totalEarn += overtime
    return totalEarn

def palabrasEnParrafo(str):
    word_count = str.strip().split()
    return len(word_count)

## Principal Program

while True:
    option = menu()
    if option == 1:
        num = readNum("Ingrese un numero: ")
        print(f"El factorial de {num} es {factorial(num)}")
    elif option == 2:
        hours = readNum("Ingrese horas trabajadas: ")
        salary = readNum("Ingrese el salario: ")
        print(f"El salario del empleado es {salarioEmpleado(hours, salary)}")
    elif option == 3:
        str = readStr("Ingrese un parrafo: ")
        print(f"El numero de palabras en el parrafo es {palabrasEnParrafo(str)}")
    elif option == 4:
        print("Thank you for using the menu")
        print("Have a great day")
        input("Press any key to continue")
        break

            
            
            
