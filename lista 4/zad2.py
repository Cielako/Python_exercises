ile = int(input("Podaj ilu elementowa ma byc lista: "))
lista = []
for i in range(0,ile):
    napis = "Podaj "+ str(i+1) +" liczbę: " 
    liczba = int(input(napis))
    lista.append(liczba)
lista_bez_powt = []
for num in lista:
    if num not in lista_bez_powt:
        lista_bez_powt.append(num)
print("Oto Twoja lista: ",lista_bez_powt)

