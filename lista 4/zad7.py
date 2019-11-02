wiersze = 10
lista=[1]
for x in range(wiersze):
    print(lista)
    lista=[lista[y]+lista[y+1] for y in range(len(lista)-1)]
    lista.insert(0,1)
    lista.append(1)