archivo = open("/home/spukN01-021/Enzo/11- Archivos/nombres.txt", "r")

texto = archivo.read()

print(texto)

archivo.seek(0)
texto2 = archivo.readline()
print(texto2)

texto3 = archivo.readlines()
print(texto3)

archivo.close()
