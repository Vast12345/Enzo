while True:

    name = input("Enter your name: ")
    status = int(input("Type your estrato: (1, 2, 3 , 4, 5)"))

    if status < 1 and status > 5:
        print("Invalid number")
    elif status == 1:
        print(f"Your name is {name} and your tarifa is 10,000")
    elif status == 2:
        print(f"Your name is {name} and your tarifa is 15,000")
    elif status == 3:
        print(f"Your name is {name} and your tarifa is 30,000")
    elif status == 4:
        print(f"Your name is {name} and your tarifa is 50,000")
    elif status == 5:
        print(f"Your name is {name} and your tarifa is 65,000")

    conti = input("Would you like to continue: Y/N ")

    if conti == "Y" or conti == "y":
        continue
    elif conti == "N" or conti == "n":
        break
    else:
        print("Invalid option")
