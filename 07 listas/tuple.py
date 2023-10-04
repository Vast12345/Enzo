def readStr(str):
    while True:
        try:
            phrase = (input(str))
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

def readNum(str):
    while True:
        try:
            num = int(input(str))
            if num < 1:
                print("Error: Invalid input, must be a positive integer")
                input("Press any key to continue")
                print("\n", "=" * 30, "\n")
                continue
            return num
        except ValueError:
            print("Error: Invalid input, must be an integer")
            input("Press any key to continue")
            print("\n", "=" * 30, "\n")

english = set()
french = set()

n = readStr("Are you from the English newspaper? Y/N "))

if n.lower() == "y":
    engRoll = readNum("What is your studen roll call")

    for i in range(n):
        english.append(readStr())

m = int(input("Are you from the French newspaper: "))

if m.lower() == "n":
    frRoll = readNum("What is your studen roll call")

    for i in range(m):
        french.add(readStr())
for i in range(m):
    french.add(readStr())

result = english - french
print(f"The Amount of students only in the English newspaper is {result}")

    



