s = "yo soy tu padre"
# print(s[7])
# print(s[-8])

# recorrer las cadenas
# for i in range(len(s)):
#     print(s[i], end=", ")


# # recorrido por elemento
# print("")
# for e in s:
#     print(e, end=", ")

# # slice 
# print("")
# print(s[2:])
# print(s[4:7])
# print(s[::-1])


# operador in
print("tu" in s)
print("yt"not in s)

# count
print(s.count("o"))

# find
print(s.find("pa"))
print(s.find("ma"))
#"Hola mundo mundo mundo".rfind('mundo') --> 17

# isdigit()
snum = "100"
print(snum.isdigit("100"))
sumnum = "100a"
print(snum.isdigit())

# isalnum()
# c = "ABC100323p"
# c.isalnum() --> True
# c.isalpha() --> False
# "Holamundo".isalpha() --> True
# "Hola mundo".islower() --> False
# "Hola mundo".isupper() --> True
# "    -    ".isspace() --> False
# "Hola Mundo".istitle() --> True
# "Hola mundo".startswith("Mola") --> False
# "Hola mundo".endswith('mundo') --> True

#split()
nombre = "Juan Daniel  Ramirez Salazar"
email = "juandanielgmail.com"
miles = "1.234.231"
print(nombre.split())
print(nombre.split("Daniel"))
print(email.split("@"))
print(miles.split("."))

# ",".join("Hola mundo") --> 'H,o,l,a, ,m,u,n,d,o

# "     Hola mundo       ".strip() --> 'Hola mundo'
# "------Hola mundo       ".strip() --> 'Hola mundo'
# "Hola mundo".replace('o','0') --> 'H0la mund0'
#