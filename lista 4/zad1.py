lista = list(input("podaj liczby do listy: "))
dlugosc = len(lista)
for d in range(dlugosc):
     lista[d] = int(lista[d])
print("Suma listy wynosi: ",sum(lista))

mnozenie = 1
for m in range(dlugosc):
     lista[m] = int(lista[m])
     mnozenie =  mnozenie * lista[m]
print ("Mnozenie wszystkich elementó z listy wynosi: ", mnozenie)
