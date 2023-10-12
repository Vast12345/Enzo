fd = open("11- Archivos/mbox-short.txt", "r")


cl = 0
cp = 0
for linea in fd:
    linea = linea.strip()
    cp += len(linea.split(" "))
    # for lin in linea.split(" "):
    #     if lin.isalnum():
    #         cp += 1
    cl += 1


fd.close()

print(f"The amount of lines is: {cl}")
print(f"The amount of words: {cp}")