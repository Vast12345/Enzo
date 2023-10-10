import random

def readStr():
    while True:
        try:
            phrase = input("Tell me your name: ")
            phrase = phrase.strip()
            if len(phrase) == 0 or phrase.isalnum() == False:
                print("Error: Invalid input, must be a string")
                input("Press any key to continue")
                print("\n", "=" * 30, "\n")
                continue
            return phrase
        except Exception as e:
            print(f"Error: Invalid input, must be a string\n{e}")
            input("Press any key to continue")
            print("\n", "=" * 30, "\n")

number = random.randint(1, 10)

def readNum():
    while True:
        try:
            num = int(input("Enter a number between 1 and 1000: "))
            if num < 1 or num > 1000:
                print("Error: Number must be between 1 and 1000")
                input("Press any key to continue")
                print("\n", "=" * 30, "\n")
                continue
            return num
        except ValueError:
            print("Error: Invalid input, must be an integer")
            input("Press any key to continue")
            print("\n", "=" * 30, "\n")

def listSort(lista):
    count = 0
    # The for loop will go through every key inside of dicProduct, and then the values within that key
    for k, v in lista:
        print("\n", "=" * 30, "\n")
        print(f"Name {k}")
        print(f"Score: {v}")
        print("\n", "=" * 30, "\n")
        
        count += 1

        if count == 10:
            return

WinnerList = {}
while True:
    number = random.randint(1, 1000)
    name = readStr()
    for i in range(1, 11):
        print(f"Tries: {i}/10")
        n = readNum()
        if n < number:
            print("FAIL: Your number is too small")
        elif n > number:
            print("FAIL: Your number is too big")
        elif n == number:
            print("Ganaste")
            WinnerList[name] = i
            break
    number = random.randint(1, 1000)
            


    option = input("Do you wish to continue? (Y/N) ")
    if option.lower() == "n":
        break
    elif option.lower() == "y":
        continue

sorted_winners = sorted(WinnerList.items(),key=lambda x: x[1])
print(listSort(sorted_winners)) 
