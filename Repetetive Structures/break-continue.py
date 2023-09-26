# break
# Calcular si un numero es primo 
# num primo: divisible por si mismo y por 1

# num = int(input("Input a number: "))

# if num < 2:
#     print("Is not a prime number.")
# elif num == 2:
#     print("Is a prime number.")
# else:
#     is_prime = True # variables banderas o switch
#     for i in range(2, num):
#         if num % i == 0:
#             is_prime = False
#             break

#     if is_prime == True:
#         print("Is prime")
#     else:
#         print("Is not prime, Lo divide",i)


# CONTINUE
# Salta una iteracion de un ciclo 

# Imprima los numeros 1 al 100 excepto los multiplo de 7
for i in range(1, 101):
    if i % 7 == 0:
        continue
    print(i, end=", ")