import os
sciezka = input("Wprowadz sciezke do pliku PESEL.txt: ")

def wczytajPlik(sciezka):
    try: 
        pesel = open(sciezka, "r", encoding="utf-8").read()#wczytanie pliku, oraz użycie enkodowania utf-8
        return pesel
    except IOError:
        print("Nie można odczytać pliku, spróbuj ponownie")


pesel = wczytajPlik(sciezka).split()
for i in range(10):
    sprKontrolna = int(pesel[i][0])*1 + int(pesel[i][1])*3 + int(pesel[i][2])*7 + int(pesel[i][3])*9 + int(pesel[i][4])*1 + int(pesel[i][5])*3 + int(pesel[i][6])*7 + int(pesel[i][7])*9 + int(pesel[i][8])*1 + int(pesel[i][9])*3  
    print(sprKontrolna)