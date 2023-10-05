

def readNote():
    while True:
        try:
            n = int(input("Input your nota: (1 - 5)"))
            if n < 1 or n > 5:
                print("Invalido")
                continue
            return n
        except ValueError:
            print("Invalido")

dicUsers = {}
while True:
    datuser = {}
    code = int(input("Input your code: "))
    if code == 999:
        break
    else:
        datuser["name"] = input("Input your name: ")
        datuser["Nota 1"] = readNote()
        datuser["Nota 2"] = readNote()
        datuser["Nota 3"] = readNote()

        dicUsers[code] = datuser




