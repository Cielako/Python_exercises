lista = []
for liczba in range(100, 401):
    cz = str(liczba)#przekonwertowanie liczby na string
    if int(cz[0])%2 == 0 and int(cz[1]) %2 == 0 and int(cz[2]) %2 == 0 :
        lista.append(cz)
print(",".join(lista))
    