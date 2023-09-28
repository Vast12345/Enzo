while True:

    try:
        num1 = int(input("Input a number: "))
        break
    except ValueError:
        print("Error. Numero entero no valido.")

while True:

    try:
        num2 = int(input("Input another number: "))
        break
    except ValueError:
        print("Error. Numero entero no valido.")


try:
    num2 = "a"
    sum = num1 + num2
    print("The sum is: ", sum)
except Exception as e:
    print("Error al intentar sumar.\n", e)