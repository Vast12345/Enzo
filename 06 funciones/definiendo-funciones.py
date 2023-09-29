# La definicion de la función
def logString(str):
    try:
        long = 0
        while str[long] != None:
            long += 1
    except:
        pass
    return long



def preparar_cafe(insumo1, insumo2):
    salida = ""
    if insumo1.lower() == "cafe" and insumo2.lower() == "agua":
        salida = "tinto"
    else:
        salida = "Dano la cafatera"
    return salida

# Uso la función
taza = preparar_cafe("cafe", "agua")
print(taza)
print(logString(taza))