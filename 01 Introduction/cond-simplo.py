# Condicional simple

sueldo = 1_100_00
sueldoMin = 1160_000

if sueldo <= sueldoMin:
    auxTrans = 140_000
else:
    auxTrans = 0

print(f"Auxilio de Transporte ${auxTrans:,}")