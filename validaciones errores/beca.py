while True:
    
    while True:
        tec_sys = 800_000
        tec_vid = 1_000_000
        tec_ani = 1_200_000
        bec_1 = 0.5
        bec_2 = 0.4



        try:
            code = input("Input your code: ")
            if code.isdigit() == False:
                print("Invalid option, your code should only consist of digits.")
                print("\n", "=" * 30)
                continue
            break
        except ValueError:
            print("Invalid option, your code should only consist of digits")

    while True: 

        try:
            name = input("Input your name: ")
            name = name.strip()
            if len(name) == 0 or name.isdigit() == True:
                print("Invalid choice, properly choose you name.")
                print("\n", "=" * 30, "\n")
                continue
            break
        except Exception as e:
            print(f"Error in inputting name\n{e}")
            print("\n", "=" * 30, "\n")
    while True:
        try:
            program = int(input("What is your academic program: \n1. Tecnico de sistemas\n2. Tecnico en desarrollo de videojuegos\n3. Tecnico de Animacion digital: "))
            if program < 1 or program > 3:
                print("Invalid option, try again")
                print("\n", "=" * 30, "\n")
                continue
            else:
                break
        except ValueError:
            print("Invalid option, choose a number that corresponds to which program you are in.")
            print("\n", "=" * 30, "\n")
    while True:
        try:
            beca = int(input("Choose which beca you are in: 1-3 "))
            if beca < 1 or beca > 3:
                print("Invalid option, choose a number from 1 through 3")
                print("\n", "=" * 30, "\n")
                continue
            break
        except ValueError:
            print("Invalid option, choose a number from 1 through 3")
            print("\n", "=" * 30, "\n")

    while True:
        if program == 1:
            if beca == 1:
                valor = tec_sys * bec_1
                print(f"Your name is: {name} and your valor matricula is ${valor}")
                break
            elif beca == 2:
                valor = tec_sys * bec_2
                print(f"Your name is: {name} and your valor matricula is ${valor}")
                break
            else:
                valor = tec_sys
                print(f"Your name is: {name} and your valor matricula is ${valor}")
                break
        elif program == 2:
            if beca == 1:
                valor = tec_vid * bec_1
                print(f"Your name is: {name} and your valor matricula is ${valor}")
                break
            elif beca == 2:
                valor = tec_vid * bec_2
                print(f"Your name is: {name} and your valor matricula is ${valor}")
                break
            else:
                valor = tec_vid
                print(f"Your name is: {name} and your valor matricula is ${valor}")
                break
        elif program == 3:
            if beca == 1:
                valor = tec_ani * bec_1
                print(f"Your name is: {name} and your valor matricula is ${valor}")
                break
            elif beca == 2:
                valor = tec_ani * bec_2
                print(f"Your name is: {name} and your valor matricula is ${valor}")
                break
            else:
                valor = tec_ani
                print(f"Your name is: {name} and your valor matricula is ${valor}")
                break
        print("\n", "=" * 30)  
    while True:  
        try:
            conti = input("Would you like to continue? Y/N ")
            if len(conti) == 0 or conti.isalnum() == False:
                print("Invalid option, choose Y to continue or N to exit.")
                continue
            break
        except Exception as e:
            print(f"Error in input\n{e}")

    if conti == "Y" or conti == "y":
        continue
    elif conti == "N" or conti == "n":
        break




