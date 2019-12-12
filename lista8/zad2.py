import os
from datetime import date

slownik = [97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122]
sciezka = input("Wprowadz sciezke do folderu, z którego chcesz odszyfrować pliki: ")

def wczytajPlik(sciezka):
        tekst = open(sciezka, "r", encoding="utf-8").read()#wczytanie pliku, oraz użycie enkodowania utf-8
        return tekst
        
def deszyfruj(zdanie,slownik):
    deszyfr = ""
    for i in zdanie:
        a = ord(i)
        if a in slownik:#jeżeli a(numer ascii jest w słowniku), to zamień i na wartość w kodzie ascii 
            if (a - klucz) < 97:#jeżeli numer klucza jest < 122 to zacznij od konca słownika i cofnij 
                litera = (a - klucz) - 97
                litera += 123
                litera = chr(litera)
                deszyfr += litera
            else:
                i = chr(a - klucz)
                deszyfr+=i
        else: deszyfr+=i
    return deszyfr

def zapisz():
    sciezka2 = sciezka + "\\" + plik
    try:
        tekst = wczytajPlik(sciezka2).lower()
    except IOError:
        print ("Blad: Nie ma takiego pliku !!!")
    else:
        today = date.today()
        deszyfrowanyTekst = deszyfruj(tekst,slownik)
        sciezkaFinal = sciezka + "\plik_deszyfrowany%" + str(klucz) + "_%" + str(today.year) + "%" + str(today.month) + "%" + str(today.day) + ".txt"
        try:
            nowy=open(sciezkaFinal,'w', encoding="utf-8")
            nowy.write(deszyfrowanyTekst)
            nowy.close()
        except OSError:
            print("Błąd otwarcia katalogu")
        except IOError:
            print("Błąd zapisu")
            
try:
    pliki = os.listdir(sciezka)
except:
    print("Błąd, nie można odczytać zawartości katalogu !!!")
else:
    for plik in pliki:
        if "plik_zaszyfrowany" in plik:
            if plik[18:20] == "10":
                klucz = int(plik[18:20])
                zapisz()
            else:
                klucz = int(plik[18:19])
                zapisz()
                   
                      
