fd = open("11- Archivos/nombres.txt", "r")

fd2 = open("11- Archivos/nombres-bak.txt", "w")

for linea in fd:
    fd2.write(linea)


fd2.close()
fd.close()

print("Process Complete")