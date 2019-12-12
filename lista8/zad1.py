import os
from datetime import date

slownik = [97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122]
sciezka = input("Wprowadz sciezke do pliku, który chcesz zaszyfrować: ")
klucz = int(input("Wprowadz klucz do szyfrowania(1-10): "))

while klucz < 1  or klucz > 10:
    klucz = int(input("Wprowadziłeś liczbę z poza zakresu,podaj liczbę z zakresu (1-10): "))#warunek powtarzany jeśli liczba jest z poza zakresu

def wczytajPlik(sciezka):
    try:
        plik = open(sciezka, "r", encoding="utf-8").read()#wczytanie pliku, oraz użycie enkodowania utf-8
        return plik
    except IOError:
        print ("Blad: Nie ma takiego pliku !!!")
        
zdanie = wczytajPlik(sciezka).lower()

def szyfruj(zdanie,slownik):
    szyfr = ""
    for i in zdanie:
        a = ord(i)
        if a in slownik:#jeżeli a(numer ascii jest w słowniku), to zamień i na wartość w kodzie ascii 
            if (a + klucz) > 122:#jeżeli numer klucza jest > 122 to zacznij od początku słownika i przesun o 10
                litera = a + klucz - 122
                litera += 96
                litera = chr(litera)
                szyfr += litera
            else:
                i = chr(a + klucz)
                szyfr+=i
        else: szyfr+=i
    return szyfr

today = date.today()
zaszyfrowanyTekst=szyfruj(zdanie,slownik)
katalog = input("Podaj ścieżkę katalogu do utworzenia zaszyfrowanego pliku: ")
if os.path.isdir(katalog):
    katalog+="\plik_zaszyfrowany%" + str(klucz) + "_%" + str(today.year) + "%" + str(today.month) + "%" + str(today.day) + ".txt"
    try: 
        nowy = open(katalog,"w",encoding="utf-8")
        nowy.write(zaszyfrowanyTekst)
        nowy.close()
    except IOError:
        print("Błąd, plik nie został zapisany")
else:
    try:
        os.mkdir(katalog)
        katalog+="\plik_zaszyfrowany%" + str(klucz) + "_%" + str(today.year) + "%" + str(today.month) + "%" + str(today.day) + ".txt"
        nowy = open(katalog,"w", encoding="utf-8")
        nowy.write(zaszyfrowanyTekst)
        nowy.close()
    except IOError:
        print("Błąd, plik nie został zapisany")
    except OSError:
        print("Nie mogę otworzyć/Utworzyć katalogu")
