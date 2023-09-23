# Calcular el factorial de un mumero
# factorial de 5 = 1 * 2 * 3 * 4 * 5 = 120

num_input = int(input("What number would you like to factorize: "))

fact = 1

for i in range(1, num_input+1):
    fact *= i # fact = fact * 1
    
print(f"The factorization of {num_input} is {fact:,}")