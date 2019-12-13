import os
sciezka = input("Wprowadz sciezke do pliku PESEL.txt: ")

def wczytajPlik(sciezka):#wczytanie pliku, oraz użycie enkodowania utf-8
    try: 
        pesel = open(sciezka, "r", encoding="utf-8").read()
        return pesel
        pesel.close()
    except IOError:
        print("Nie można odczytać pliku, spróbuj ponownie")

pesel = wczytajPlik(sciezka).split()

def fsprawdzKontrolna(i):#Funkcja sprawdzająca poprawność peselu
    sprKontrolna = int(pesel[i][0])*1 + int(pesel[i][1])*3 + int(pesel[i][2])*7 + int(pesel[i][3])*9 + int(pesel[i][4])*1 + int(pesel[i][5])*3 + int(pesel[i][6])*7 + int(pesel[i][7])*9 + int(pesel[i][8])*1 + int(pesel[i][9])*3
    kontrolna = str(sprKontrolna)
    if len(kontrolna) == 2:
        kontrolna = 10 - int(kontrolna[1])
        return kontrolna
    elif len(kontrolna) == 3:
        kontrolna = int(kontrolna) % 10
        if kontrolna == 0:
            kontrolna = str(kontrolna)
            return kontrolna
        else: 
            kontrolna = 10 - int(kontrolna)
            return kontrolna
    
    
for i in range(10):
    if str(fsprawdzKontrolna(i)) == pesel[i][10]:
        print(pesel[i],"Pesel jest poprawny")
        if int(pesel[i][0:2]) <= 99 and int(pesel[i][2:4]) > 20 and int(pesel[i][2:4]) <= 32:
            rok = "20" + pesel[i][0:2]
            if int(pesel[i][2:4]) > 20 and int(pesel[i][2:4]) < 30:
                miesiac = "0" + pesel[i][3:4]
            elif int(pesel[i][2:4]) > 29 and int(pesel[i][2:4]) <= 32: 
                miesiac = "1" + pesel[i][3:4]
        elif int(pesel[i][0:2]) <= 99 and int(pesel[i][2:4]) >= 1 and int(pesel[i][2:4]) <= 12:
            rok = "19" + pesel[i][0:2]
            if int(pesel[i][2:4]) >= 1 and int(pesel[i][2:4]) < 10:
                miesiac = "0" + pesel[i][3:4]
            elif int(pesel[i][2:4]) > 9 and int(pesel[i][2:4]) <= 12: 
                miesiac = "1" + pesel[i][3:4] 
        dzien = pesel[i][4:6]
        if int(pesel[i][9]) % 2 == 0:
            plec = "Kobieta"
        else: 
            plec = "Mężczyzna" 
        print("Data urodzenia:", rok + "-" + miesiac + "-" + dzien + ", Płeć: " + plec)
    else: 
        print(pesel[i],"Pesel jest niepoprawny")
    sciezka = os.getcwd()
    print("Tworzę plik w",sciezka)
    dobrePesele=open(sciezka+'\poprawnePESELE.txt','a')
    dobrePesele.write(pesel[i]+":\n data urodzenia "+ dzien + '-' + miesiac + '-' + rok +';\t płeć: '+ plec +'\n')
    dobrePesele.close()
       
            
        
   