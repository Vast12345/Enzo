n = int(input("How many users? "))

pas_exprt = 0.3
pas_nova = 0.2
enco_exprt = 0.2
enco_nova = 0.15



num_exprt = 0
num_nov = 0
total_consumer = 0

for i in range(1, n+1):
    celula = int(input("Input your celula"))
    name = input("Input your name")
    clase = int(input("Which clase conducter are you?:\n1. Expert\n2. Novato"))
    valor_pasa = int(input("el valor total por concepto de pasajes del mes: $"))
    valor_enco = int(input("el valor total por concepto encomiendas del mes: $"))

    
    if clase == 1:
            num_exprt += 1
    elif clase == 2:
            num_nov += 1
    
    if clase == 1:
        pasa_pay = valor_pasa * pas_exprt
        enco_pay = valor_enco * enco_exprt
        total_pay = pasa_pay + enco_pay
        print(f"You have to pay ${pasa_pay} for pasajes and ${enco_pay} for Encomiendas")
        print("\n", "=" * 40)
    elif clase == 2:
        pasa_pay = valor_pasa * pas_nova
        enco_pay = valor_pasa * enco_nova
        total_pay = pasa_pay + enco_pay
        print(f"You have to pay ${pasa_pay} for pasajes and ${enco_pay} for Encomiendas")
        print("\n", "=" * 40)
    else:
        print("Invalid option")
    
    total_consumer += total_pay
print("\n", "=" * 40)
print(f"The total pay is ${total_consumer}\nThe amount of experts are: {num_exprt}, and the number of novatos are: {num_nov}")



