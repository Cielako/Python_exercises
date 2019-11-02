zakres = range(3,100,3)
lista =[]
for x in zakres:
    lista.append(x)
del lista[4::3]
print ("wypisuje listę, która ma usunięty co 3 element i zaczyna od 5 elementu: ",lista)
dlugosc_listy = len(lista)
print("Średnia arytmetyczna otrzymanej listy wynosi: ",sum(lista)/dlugosc_listy)
