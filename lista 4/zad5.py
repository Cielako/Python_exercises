from math import factorial
ile_element=int(input("Ilu elementowa ma byc lista: "))
lista = []
for i in range(0,ile_element):
    napis = "Podaj " + str(i+1) + " liczbę: "
    liczba = int(input(napis))
    lista.append(liczba)
print("Lista dla której wykonamy permutację każdej liczby w tej liście to: ",lista)
dlugosc_listy = len(lista)
for i in range(0,dlugosc_listy):
    print("Permutacja dla liczby:",lista[i],"to", factorial(lista[i]))

