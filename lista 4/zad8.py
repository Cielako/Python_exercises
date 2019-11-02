liczba = int(input("Podaj liczbę do wypisania szeregu harmonicznego: "))

def szereg_harmoniczny(liczba):
    szereg=0
    if liczba < 2:
        print("Szereg harmoniczny: ",liczba)
    else:
        for x in range(1,liczba+1):
            szereg += (1/x) 
        print(szereg)
szereg_harmoniczny(liczba)
