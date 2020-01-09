from xml.dom import minidom as mini
import os
class Kalkulator_walut:
    
    def __init__(self,sciezka):
        self.sciezka = mini.parse(sciezka)
    
    def dane(self):
        kursy = {}
        przeliczniki = {}
        
        nazwaTag = self.sciezka.getElementsByTagName('nazwa_waluty')
        przelicznikTag = self.sciezka.getElementsByTagName('przelicznik')
        kodWalutyTag = self.sciezka.getElementsByTagName('kod_waluty')
        kursSredniTag = self.sciezka.getElementsByTagName('kurs_sredni')
         
        for kod, srkurs in zip(kodWalutyTag, kursSredniTag):#zip umożliwa wykonanie kilku pętli, przy użyciu 1 fora
            kod = str(kod.firstChild.data)
            srkurs = float(str(srkurs.firstChild.data.replace(',','.')))
            kursy.update({kod : srkurs})
            
        for przelicznik, srkurs in zip(przelicznikTag, kursSredniTag):
            przelicznik = float(przelicznik.firstChild.data)
            srkurs = float(str(srkurs.firstChild.data.replace(',','.')))
            przeliczniki.update({srkurs : przelicznik}) 
        return kursy,przeliczniki
    
    def listaKursow(self):
        dane = Kalkulator_walut("baza.xml")
        kursy,przeliczniki  = dane.dane()
        print("Obecne Kursy")
        for kod, kurs, przelicznik in zip(kursy.keys(), kursy.values(), przeliczniki.values()):
            print(kod + " " + str(przelicznik) + " : " + str(kurs) + " zł")
            
    def plnInna(self,ilosc,inna):
        dane = Kalkulator_walut("baza.xml")
        kursy,przeliczniki  = dane.dane()
        
        if inna in kursy.keys():
            wynik = float((ilosc / kursy[inna]) * przeliczniki[ kursy[inna]])
            print("Po wymianie otrzymasz:" + " " + str(round(wynik,2)) + inna )
        else:
            print("Nieprawidłowy kod waluty!!!")
    
    def inna_na_Inna(self,z,na,ilosc):
        dane = Kalkulator_walut("baza.xml")
        kursy,przeliczniki  = dane.dane()
        if z and na in kursy.keys():
            naPln = float((ilosc * kursy[z]) / przeliczniki[kursy[z]])
            wynik = float((naPln / kursy[na]) * przeliczniki[kursy[na]])
            print("Po wymianie otrzymasz:" + " " + str(round(wynik,2)) + na )
            
        
        
akcja = Kalkulator_walut("baza.xml")
wybor = int(input("Proszę wybrać 1 z 3 następujących opcji\n1.Lista aktualnych kursów\n2. Zamiana zł. na inną walutę\n3. Inna na inną\nWybór: "))
if wybor == 1:
    os.system('cls')
    print(akcja.listaKursow())
elif wybor == 2:
    os.system('cls')
    ilosc = float(input("Podaj ile złotówek chcesz wymienić na inną walutę: "))
    inna = input("Na jaką walutę wymienić?: ")
    print(akcja.plnInna(ilosc,inna))
    
elif  wybor == 3:
    os.system('cls')
    inna1 = input("Jaką walutę chcesz wymienić?: ")
    inna2 = input("Na jaką walutę wymienić?: ")
    ilosc = float(input("Podaj jaką kwotę chcesz wymienić na inną walutę: "))
    print(akcja.inna_na_Inna(inna1,inna2,ilosc))
else:
    print("Podano nieprawidłową opcję, kończę program")


       
       
       


        
    