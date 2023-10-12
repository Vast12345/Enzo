fd = open("11- Archivos/mbox-short.txt", "r")
fd2 = open("11- Archivos/email-simulation-exercise.txt", "w")

setEmail = set() 
for linea in fd:
    if linea.startswith("To:"):
        #cl += 1
        #email = linea.split()[1]
        #print(email)
        setEmail.add(linea.split()[1])


for email in setEmail:
    fd2.writelines([f"{email} sent [ok]\n"])

fd2.close()
fd.close()
