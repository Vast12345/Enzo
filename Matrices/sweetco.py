def calcularProdMaxIngresosSem(matVtas, matPrecios):
    fil = len(matVtas)
    lstTotVtas = [0] * fil
    for f in range(fil):
        lstTotVtas[f] = sum(matVtas[f]) * matPrecios[f]
    
    # print(lstTotVtas)
    maxVtas = max(lstTotVtas)
    prodMaxVtas = lstTotVtas.index(maxVtas) + 1
    return prodMaxVtas

def calcularDiaMaxIngreso(matVtas, matPrecios):
    fila = len(matVtas)
    col = len(matVtas[0])
    lstCol = [0] * 7
    for product in range(fila):
        for day in range(col):
            lstCol[day] += (matVtas[product][day]) * matPrecios[product]
    print(lstCol)
    maxLstCol = max(lstCol)
    dayMaxCol = lstCol.index(maxLstCol) + 1
    return dayMaxCol
        


matPrecios = [1500, 5000, 6500, 2500, 22500]
matVtas = [ [100, 88, 92, 94, 85, 110, 118],
            [30, 42, 31, 32, 38, 40, 37],
            [23, 35, 39, 45, 55, 60, 61],
            [45, 50, 56, 65, 47, 57, 68],
            [18, 25, 33, 21, 22, 28, 32] ]

prodMaxIngSem = calcularProdMaxIngresosSem(matVtas, matPrecios)
print(f"The product with the most amount of gross income in the week is the {prodMaxIngSem}th product.")
days = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]
dayMaxIng = calcularDiaMaxIngreso(matVtas, matPrecios)
print(f"The day with the most sales is the {days[dayMaxIng]} day")