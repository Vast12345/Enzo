fd = open("11- Archivos/mbox-short.txt", "r")


setEmail = set() 
for linea in fd:
    if linea.startswith("To:"):
        #cl += 1
        #email = linea.split()[1]
        #print(email)
        setEmail.add(linea.split()[1])

fd.close()
for email in setEmail:
    print(f"{email} sent [ok]")