from random import randint
import time
lista_100 = []
lista_200 = []
lista_300 = []

def losuj(lista,ilosc):
    for i in range(0,ilosc):
        losowe = randint(0,20)
        lista.append(losowe)
    print(lista)

def sortuj(lista):
    czas = time.time()
    for i in range(1,len(lista)):
        klucz = lista[i]#pobranie zawartości o indeksie i
        j = i - 1 #ustalenie poprzedniego indeksu
        while j >= 0 and klucz < lista[j]:#dopóki j >= 0 i wartość(klucz) jest większa od wartości o indeksie j
            lista[j + 1] = lista[j]#ustawiamy wartość o indeksie (j+1) na indeks j
            j = j - 1#aktualizowanie wartości j o 1 mniejszą
        lista[j + 1] = klucz#przypisanie wartości o indeksie j+1 zmiennej klucz
    print("Czas mojej aplikacji zajął:",time.time()-czas)
    print(lista)


losuj(lista_100,100)
losuj(lista_200,200)
losuj(lista_300,300)

sortuj(lista_100)
print("\n\n")
sortuj(lista_200)
print("\n\n")
sortuj(lista_300)
