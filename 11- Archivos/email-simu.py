fd = open("11- Archivos/mbox-short.txt", "r")
fd2 = open("11- Archivos/email-simulation-exercise.txt", "w")

lstEmail = []
for linea in fd:
    if linea.startswith("From:"):
        #cl += 1
        #email = linea.split()[1]
        #print(email)
        email = linea.split()[1]
        if email not in lstEmail:
            lstEmail.append(email)
            
# for email in setEmail:

for i in range(len(lstEmail)-1, 0, -1):
    msj = f"{lstEmail[i]} sent [ok]"
    print(msj)
    fd2.write(msj+"\n")

fd2.close()
fd.close()
