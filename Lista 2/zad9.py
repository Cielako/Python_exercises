from itertools import chain
liczby = [[2, 4, 3], [1, 5, 6], [9], [7, 9, 0]]
lista = []
lancuch = chain(liczby)
for it in lancuch:
    for element in it:
        lista.append(element)
print(lista)
    
