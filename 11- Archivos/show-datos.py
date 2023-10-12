fd = open("11- Archivos/datos-empleado.txt", "r")
# text = fd.readlines()
# print(text)

# The for data loop reads each line similar to how the .readlines() function works.
for data in fd:
    if not data.startswith("ID"):
        dats= data.split(",")
        print(f"ID: {dats[0]}\nName: {dats[1]}\nAge: {dats[2]}\nSexo: {dats[3]}\nPhone: {dats[4]}\n")
        print("=" * 30)


fd.close()



