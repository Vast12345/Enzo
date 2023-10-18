lista = [{"300": {"title": "Tattoo in the shade", "author": "Lorenzo", "price": 10}}, {"123": {"title": "Shining", "author": "King", "price": 20}}, {"100": {"title": "el dragon de vapor", "author": "Kevin", "price": 1}}]

listTitle = []
for i in range(len(lista)):
    data = lista[i]
    listTitle.append(list(data.keys()))
listTitle = sorted(listTitle)
print(listTitle)