def order(numeros):
    for i in range(0, n-1):
        for j in range (i+1, n):
            if numeros[i]>numeros[j]:
                t=numeros[i]
                numeros[i] = numeros[j]
                numeros[j] = t
    return numeros

n = int(input("Number: "))
numeros = []
for i in range(n):
    num=int(input("Numbero: "))
    numeros.append(num)

print(f"list numbers: {numeros}")
numeros = order(numeros)
print(f"Order list numbers : {numeros}")