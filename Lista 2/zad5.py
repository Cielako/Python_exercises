napis = input("Podaj jakiś napis: ")
indeks = int((len(napis)))
indeks= round(indeks/2)
napis2 = input("Podaj kolejny napis: ")
wypisz_linię = napis[:indeks] + napis2 + napis[indeks:]
print(wypisz_linię)
