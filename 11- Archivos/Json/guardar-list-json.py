import json

fd = open("11- Archivos/Json/lista.json", "r")

lst = []

lst = json.load(fd)

for e in lst:
    print(f"Name: {e['nombre']}")
    print(f"Edad: {e['edad']}")
    print("-" * 30)


fd.close()