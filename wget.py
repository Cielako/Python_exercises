import urllib.request
def pobierz(adres):
    wczytaj = urllib.request.urlopen(adres)
    try:    
        print("Strona została znaleziona", wczytaj)
        zawartosc = wczytaj.read()
    if adres.endswith('/'):
        nowy_plik = open('index.html', w+)
        nowy_plik.write(zawartosc.read())
        nowy_plik.close()
    else:
        nowy_plik = open(adres + '.html', w+)
        nowy_plik.write(zawartosc.read())
        nowy_plik.close()
    except:
        print(strona + "  Error 404 - Strona nie została odnaleziona :(")

pobierz('https://docs.python.org/3/library/urllib.request.html')