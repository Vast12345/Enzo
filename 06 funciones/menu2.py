import math

def menu():
    while True:
        try:
            print("*** MENU ***")
            print("1- Calculate combinatations")
            print("2- Convert text to number")
            print("3- Calculate IVA for a factura")
            print("4- Exit")
            option = int(input("Option: "))
            if option < 1 or option > 4:
                print("Invalid option")
                input("Type anything to continue")
                print("\n", "=" * 30, "\n")
                continue
            return option
        except ValueError:
            print("Invalid option")
            input("Type anything to continue")
            print("\n", "=" * 30, "\n")

def readNum(str):
    while True:
        try:
            num = int(input(str))
            if num < 0:
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

def Combination(n, k):
    try:
        combi = math.factorial(n) / (math.factorial(k) * math.factorial(n - k))
        return combi
    except ValueError:
        pass


def Convert(msj):
    text = ''.join(char for char in msj if char.isdigit())
    return text

def IVA(a, b):
    b /= 100
    factura = a + (a * b)
    return factura

while True:
    option = menu()
    if option == 1:
        n = readNum("Ingrese primer numero entero: ")
        k = readNum("Ingrese segundo numero entero: ")
        combi = Combination(n, k)
        if combi is not None:
            print(f"El numero de combinaciones es {Combination(n, k)}")
            print("\n", "=" * 30, "\n")
        else:
            print("Error: Invalid input")
            print("\n", "=" * 30, "\n")
    elif option == 2:
        msj = input("Input a text.")
        print(f"El texto convertido a numero es {Convert(msj)}")
        print("\n", "=" * 30, "\n")
    elif option == 3:
        a = readNum("Ingrese Factura:  ")
        b = readNum("Ingrese IVA:  ")
        print(f"El valor del IVA es {IVA(a, b)}")
        print("\n", "=" * 30, "\n")
    elif option == 4:
        print("Thank you for using the menu")
        print("Have a great day")
        input("Press any key to continue")
        break

