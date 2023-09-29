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

n = input("Input a collection of letters: ")

if n.isalpha() == False:
    print("Invalid option")

result = ""
loop = 0

# for e in range(len(n)):
#         current_char = n[e]
#         result += current_char

#         if e < len(n) - 1 and n[e] == n[e + 1]:
#             e += 2
#         else:
#              e += 1
while loop < len(n):
    # current_char = n[loop]
    # result += current_char

    if loop < len(n) - 1 and n[loop] == n[loop + 1]:
        loop += 2
        current_char = n[loop]
        result += current_char
    else:
        loop += 1
        current_char = n[loop]
        result += current_char

        
            



print(f"The result of the collection of letters is {result}")



 
