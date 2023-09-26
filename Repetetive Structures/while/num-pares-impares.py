num = int(input("Input a number: "))
cpares = 0
cimpares = 0
while num != -1:
    if num % 2 == 0:
        print("The number is par")
        cpares += 1
    else:
        print("The number is impar")
        cimpares += 1

    num = int(input("Input a number: "))
print("\n", "=" * 30)
print("The amount of pares is: ", cpares)
print("The amount of impares is: ", cimpares)