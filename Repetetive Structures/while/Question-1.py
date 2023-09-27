# Empresa-Comision

while True:

    comi_puerta =  0.2
    comi_tele = 0.15
    comi_eje = 0.25


    cel_ciu = int(input("Input your Cedula de ciudadania: "))
    name = input("Input your name: ")
    vende = int(input("Input your vendedor\n1. Puerta a puerta\n2. Telemercadeo\n3. Ejecutivo de ventas\n: "))
    valor_venta = int(input("Input your valor ventas realizada en el mes: $"))

    if cel_ciu == -1:
        print("You can't")
        break
    else:
        if vende == 1:

            comi_venta = valor_venta * comi_puerta
            valor_total = valor_venta - comi_venta
            print(f"Your valor total del mes is ${valor_total}\nWhat you need to pay for commissions: ${comi_venta}")
        elif vende == 2:
            comi_venta = valor_venta * comi_tele
            valor_total = valor_venta - comi_venta
            print(f"Your valor total del mes is ${valor_total}\nWhat you need to pay for commissions: ${comi_venta}")
        elif vende == 3:
            comi_venta = valor_venta * comi_eje
            valor_total = valor_venta - comi_venta
            print(f"Your valor total del mes is ${valor_total}\nWhat you need to pay for commissions: ${comi_venta}")
        else:
            print("Invalid option")


        conti = input("Would you like to continue? Y/N ")

        if conti == "Y" or conti == "y":
            continue
        elif conti == "N" or conti == "n":
            break
        else:
            print("Invalid option")




