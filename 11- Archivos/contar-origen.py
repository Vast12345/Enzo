# un programa que cuente y muestre los correos de origens distinos que hayen el mbox.txt.
fd = open("11- Archivos/mbox-short.txt", "r")


cl = 0
setEmail = set() 
for linea in fd:
    if linea.startswith("From:"):
        #cl += 1
        #email = linea.split()[1]
        #print(email)
        setEmail.add(linea.split()[1])


fd.close()
cl = len(setEmail)
print(f"The amount of emails in mbox.txt is: {cl}")

for email in sorted(setEmail, reverse=False, key=lambda x: len(x)):
    print(email)