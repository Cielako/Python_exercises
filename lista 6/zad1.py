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
    print("Wpisz sowje liczby ponownie, aby otrzymać informacje o trójkącie")
    import trojkat
    
else:
    print("Z podanych długości nie da się utworzyć trójkąta(Kończę program !!)")