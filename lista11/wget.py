import urllib.request
def pobierz(adres):
    try:
        print("Strona została znaleziona", urllib.request.urlopen(adres))
        zawartosc = str(urllib.request.urlopen(adres).read())    
        if adres.endswith('/'):
            nowy_plik = open('index.html', 'w+')
            nowy_plik.write(zawartosc)
            nowy_plik.close()
        else:
            nazwa = adres.strip('https://')
            nazwa = nazwa.split('/',1)[0]
            nowy_plik = open(nazwa + '.html', 'w+')
            nowy_plik.write(zawartosc)
            nowy_plik.close()
    except:
        print(adres + "  Error 404 - Strona nie została odnaleziona :(")
    
pobierz("https://www.google.com")