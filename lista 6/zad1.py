dlugosci_bokow = []
i=0
while True:
    liczba = float(input("Podaj dlugość "+str(i+1)+" boku:"))
    dlugosci_bokow.append(liczba)
    i+=1
    if(i>2):
        break
if(dlugosci_bokow[0] < (dlugosci_bokow[1]+dlugosci_bokow[2]) and dlugosci_bokow[1] < (dlugosci_bokow[0]+dlugosci_bokow[2]) and dlugosci_bokow[2] < (dlugosci_bokow[0]+dlugosci_bokow[1])):
    print("Podane długości boków pozwalają utworzyć trójkąt")
    boki = dlugosci_bokow
    import os
    os.system('cls||clear')
    from trojkat import *
    print("Obwód tego trójkąta wynosi:",obwod(boki[0],boki[1],boki[2]))
    print("Pole tego trojkata wynosi:",pole(boki[0],boki[1],boki[2]))
    print("Ten trójkąt jest " + rrr(boki[0],boki[1],boki[2]))
    print("Ten trójkąt jest " + por(boki[0],boki[1],boki[2]))
    
else:
    print("Z podanych długości nie da się utworzyć trójkąta(Kończę program !!)")