# num = input("Ingrese el numero: ")

# if num.startswith("+") and num.count("-") == 2:
#     partes = num.split("-")
#     print("El telefono es: ", partes[1])
# else:
#     print("Error. El numero no cumple con el formato")

# word = input("Type in a word: ")

# if word == word[::-1]:
#     print("The word is a palindroma")
# else:
#     print("The word is not a palindroma")

# birth = input("Input your date of birth")

# parts = birth.split("/")
# if len(parts[0]) == 2 and \
#     len(parts[1]) == 2 and \
#         len(parts[2]) == 4:
    
#     truth = True
#     for p in parts:
#         if not p.isdigit():
#             truth = False
#             break

#     if truth:
#         print(f"day: {parts[0]}, month: {parts[1]}, year: {parts[2]}")
#     else:
#         print("Invalid format")
# else:
#     print("Invalid format")

n = input("Input a collection of letters")

for i in n:
    if n([i]) == n([i+1]):
        n.split()[i]
