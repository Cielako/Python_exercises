liczba = int(input("Podaj liczbę(n) do wypisania sumy szeregu harmonicznego dla n początkowych liczb: "))

def szereg_harmoniczny(liczba):
    szereg = 0
    if liczba < 2:
        print("Szereg harmoniczny: ",liczba)
    else:
        for x in range(1,liczba+1):
            szereg += (1/x) 
        print(szereg)
szereg_harmoniczny(liczba)
