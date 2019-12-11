import os
from datetime import date

slownik = [97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122]
sciezka = input("Wprowadz sciezke: ")
klucz = int(input("Wprowadz klucz do szyfrowania(1-10): "))



def FileCheck(sciezka):
    try:
        f = open(sciezka, "r", encoding="utf-8").read()#wczytanie pliku, oraz użycie enkodowania utf-8
        return f
    except IOError:
        print ("Blad: Nie ma takiego pliku")
        
zdanie = FileCheck(sciezka).lower()

def szyfruj(zdanie,slownik):
    szyfr = ""
    for i in zdanie:
        a = ord(i)
        if a in slownik:#jeżeli a(numer ascii jest w słowniku), to zamień i na wartość w kodzie ascii 
            if (a + klucz) > 122:
                litera = a + klucz - 122
                litera += 96
                litera = chr(litera)
                szyfr += litera
            else:
                i = chr(a + klucz)
                szyfr+=i
        else: szyfr+=i
    return szyfr
print(szyfruj(zdanie,slownik))