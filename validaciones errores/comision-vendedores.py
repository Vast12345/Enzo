while True:
    try:
        n = input("How many users: ")
        if n.isdigit() == False:
            print("Invalid, input how many users there are.")
            continue
        break
    except ValueError:
        print("Error, input how many users here are.")

puerta_comi = 0.2
puerta_valor = 1.2
tele_comi = 0.15
tele_valor = 1.15
eje_comi = 0.25
eje_valor = 1.25

total_pay = 0
loop = 0


while loop < eval(n):

    while True:
        try:
            cedula = input("Input your cedula de ciudania: ")
            if cedula.isdigit() == False:
                print("Your cedula should only consist of numbers.")
                print("\n", "=" * 30, "\n")
                continue
            # num_cedula = cedula
            # if num_cedula < 0:
                # print("Not allowed.")
            break
        except Exception as e:
            print("Error: correctly input your cedula", e)
            print("\n", "=" * 30, "\n")
        
    while True:
        try:
            name = input("Input your name: ")
            name = name.strip()
            if len(name) == 0 or name.isdigit() == True:
                print("Input your correct name.")
                print("\n", "=" * 30, "\n")
                continue
            break
        except Exception as e:
            print(f"There was an error.\n{e}")
            print("\n", "=" * 30, "\n")
        
    while True:
        try:
            vende = int(input("Input what type of vendedor you are: \n1. Puerta a Puerta.\n2. Telemarcaedo.\n3. Ejecutivo de ventas.\n: "))
            if vende < 1 or vende > 3:
                print("Invalid option, choose from 1 through 3.")
                print("\n", "=" * 30, "\n")
                continue
            break
        except ValueError:
            print("Invalid option, must choose from 1 through 3.")
            print("\n", "=" * 30, "\n")

    while True:
        try:
            valor_venta = int(input("Input your valor de ventas realizado en el mes: $"))
            if valor_venta < 1:
                print("Error, input your valor de ventas. ")
                print("\n", "=" * 30, "\n")
                continue
            break
        except ValueError:
            print("Error, input your valor de ventas.")
            print("\n", "=" * 30, "\n")
        
    while True:
        if vende == 1:
            commission = valor_venta * puerta_comi
            valor_total = valor_venta * puerta_valor
            print(f"Name: {name}\nYour commission will cost ${commission} and your valor total de la ventas del mes is ${valor_total}")
            print("\n", "=" * 30, "\n")
            break
        elif vende == 2:
            commission = valor_venta * tele_comi
            valor_total = valor_venta * tele_valor
            print(f"Name: {name}\nYour commission will cost ${commission} and your valor total de la ventas del mes is ${valor_total}")
            print("\n", "=" * 30, "\n")
            break
        elif vende == 3:
            commission = valor_venta * eje_comi
            valor_total = valor_venta * eje_valor
            print(f"Name: {name}\nYour commission will cost ${commission} and your valor total de la ventas del mes is ${valor_total}")
            print("\n", "=" * 30, "\n")
            break

    total_pay += valor_total
    loop += 1
    
print("\n", "=" * 30, "\n") 
print(f"The total pay for all the users is ${total_pay}")

        









