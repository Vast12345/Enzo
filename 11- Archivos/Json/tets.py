lista = [{"300": {"title": "Tattoo in the shade", "author": "Lorenzo", "price": 10}}, {"123": {"title": "Shining", "author": "King", "price": 20}}, {"100": {"title": "el dragon de vapor", "author": "Kevin", "price": 1}}]

listTitle = []
for item in lista:
    keys = list(item.keys())[0]
    title = item[keys]['title']
    listTitle.append(title)

print(listTitle)