milista = [] # lista vacia 
milista2 = list() # lista vacia

nom_campers = ["Juan", "Yulieth", "Lorenzo", "Manuel", "David"]
print(nom_campers)
print(nom_campers[1])
nom_campers[1] = "Julieth"
print(nom_campers[1])

# SLICES
print(nom_campers[2:4])
print(nom_campers[::-1])

nom_camper_juan = ["Daniela", "Maria", "Juliana", "Sandra", "Carolina"]
print(nom_camper_juan)
# nom_campers += nom_camper_juan
# print(nom_campers)

# METODOS DE LISTAS
nom_campers.append("Kevin")
print(nom_campers)

nom_campers.extend(nom_camper_juan)
print(nom_campers)
print(nom_campers[-1])
nom_campers.insert(1, "Carlos")
print(nom_campers)

nom_campers.pop()
print(nom_campers)

nom_campers.pop(-3)
print(nom_campers)

nom_campers.remove("Sandra")

nom_campers.sort()
print(nom_campers)

nom_campers.insert(2, "Daniel")
nom_campers.sort()
print(nom_campers)

# list2 = [0,1,15,"115"]
# list2.sort()
# print(list2)
nom_campers.sort(reverse=True)
print(nom_campers)