def readNum():
    while True:
        try:
            n = int(input("Input a number: "))
            if n < 1:
                print("Invalid option, number must be greater than 2.")
                input()
                continue
            return n
        except ValueError:
            print("Error: input must be an integer")
            input()

def prime_range(n, m):
    list = []
    number = 0
    for i in range(n, m+1):
        if number % i == 0:
            list.append(number)
            number += 1
    return list

print(prime_range(readNum(), readNum()))