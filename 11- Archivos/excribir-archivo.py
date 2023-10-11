archivo = open("/home/spukN01-021/Enzo/11- Archivos/salas.txt", "w")

archivo.write("sputnik\n\t")
archivo.write("apolo\n")

archivo.writelines(["houston\n", "artemis\n"])

archivo.close()