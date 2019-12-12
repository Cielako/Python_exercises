from random import randint
import os

sciezka = os.getcwd()
print("Tworzę plik w",sciezka)
plik=open(sciezka+'\PESEL.txt','w')
plik.close()
     
for i in range(10):
    pesel = "" 
    rok = str(randint(1900,2099))
    pesel += str(rok[1:3])
    
    if int(rok) < 2000:
        miesiac = str(randint(1,12))
        if int(miesiac) < 10:
            pesel += "0" + miesiac
        else:
            pesel += miesiac
    elif int(rok) >= 2000:
        miesiac = str(randint(21,32))
        pesel += miesiac
        
    dzien  =  str(randint(1,31))
    if int(dzien) < 10:
        pesel += "0" +  dzien
    else:
        pesel += dzien
        
    porzadkowa = str(randint(0,9999))
    if int(porzadkowa) < 10:
        pesel += "000" + porzadkowa
    elif  int(porzadkowa) < 100:
        pesel += "00" + porzadkowa  
    elif int(porzadkowa) < 1000:
        pesel += "0" + porzadkowa
    else:
        pesel += porzadkowa
    kontrolna = str(randint(0,9))
    pesel += kontrolna 
    
    plik_Pesel = open(sciezka+"\PESEL.txt","a")
    plik_Pesel.write(pesel+"\n")
    plik_Pesel.close()    
    

    
    
    
    
    
        
    