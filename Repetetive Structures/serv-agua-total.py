n = int(input("How many users ?"))

totalConsumo = 0
for i in range(1, n+1):
    print(f"\nData of user #{i}")
    code = input("Code? ")
    name = input("Name? ")
    state = input("State [V: vigente o S: Supendido]?")
    estr = int(input("Estrato [1 al 6]? "))
    con = float(input("Consumo agua al mes [cm3]? "))
    
    if state == "V" or state == "v":
        # calcular la tarifa basica
        if estr == 1:
            tbas = 10000
        elif estr == 2:
            tbas = 20000
        elif estr == 3:
            tbas = 30000
        elif estr == 4:
            tbas = 45000
        elif estr == 5:
            tbas = 60000
        elif estr == 6:
            tbas = 70000
        else:
            tbas = 0
        # calcular el valor del consumo
        valcons = con * 200

        # calcular el valor a pagar
        valpagar = tbas + valcons
        
        # calcular el valor total a pagar de todos lus usuaros
        totalConsumo += valpagar

        # imprimir el informe del usuario
        print("\n", "=" * 40)
        print("\tNombre: ", name)
        print(f"\tValor de tarifa basica ${tbas:,.0f}")
        print(f"\tValor consumo: ${valcons:,.0f}")
        print(f"Valor de la factura de agua: ${valpagar:,.0f}")


# Imprimir valor total a pagar de todos los usuarios
print("\n", "=" * 40)
print(f"\tValor total:  ${totalConsumo:,.0f}")
