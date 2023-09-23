# capturar las notas de un curso y calcular el promedio de estas.
# Mostrar en pantalla el resulto del promedio

cant = int(input("Amount of notes: "))

sumNote = 0
for i in range(1, cant+1): #range(1, cant+1)
    note = float(input("Input the note #",i))
    sumNote = sumNote + note # sumNote += note

prom = sumNote / cant
print(f"The promedio of the notes is: {prom:.1f}")

