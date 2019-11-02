#1 sposób
liczba = int(input("Podaj liczbę: "))
if(liczba%2 == 0):
    print(liczba, " jest parzysta")
else:
    print(liczba, " jest nieparzysta")
#2 sposób
reszta = liczba%2
k = ("Liczba jest parzysta","Liczba jest nieparzysta")
print(k[reszta]) 