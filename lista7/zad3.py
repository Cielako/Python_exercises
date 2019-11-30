from zad2 import lista_100,lista_200,lista_300
import time

def sortowanie_babelkowe(lista):
    czas = time.time()
    for i in range(len(lista)):
        j = i - 1
        while j > i:
            if lista[j] > lista[i]:
                tmp = lista[j]
                lista[j] = lista[j-1]
                lista[j-1] = tmp
            j-=1
    return lista
    print("Czas mojej aplikacji zajął:",time.time()-czas)

sortowanie_babelkowe(lista_100)
print("\n\n")
sortowanie_babelkowe(lista_200)
print("\n\n")
sortowanie_babelkowe(lista_300)