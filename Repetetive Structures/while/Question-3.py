# Transrapido-Valor

n = int(input("How many users? "))

a = 25.000
b = 35.000
c = 50.000




num_a = 0
num_b = 0
num_c = 0
total_consumer = 0

for i in range(1, n+1):
    celula = int(input("Input your celula: "))
    name = input("Input your name: ")
    docente = (input("Which category docente are you: A, B, C.  "))
    hours = int(input("How many hours do you use the laboratory: "))


    
    if docente == "A" or docente == "a":
        num_a += 1
    elif docente == "B" or docente == "b":
        num_b += 1
    elif docente == "C" or docente == "c":
        num_c += 1
    
    if docente == "A" or "a":
        valor_pay = hours * a
        print(f"You have to pay ${valor_pay}")
        print("\n", "=" * 40)
    elif docente == "B" or "b":
        valor_pay = hours * b
        print(f"You have to pay ${valor_pay}")   
        print("\n", "=" * 40)
    elif docente == "C" or "c":
        valor_pay = hours * c
        print(f"You have to pay ${valor_pay}")
    else:
        print("Invalid option")
    
    total_consumer += valor_pay
print("\n", "=" * 40)
print(f"The total pay is ${total_consumer}\nThe amount of docente A: {num_a}, the amount of docente B: {num_b}, and the amount of docente C: {num_c}")

