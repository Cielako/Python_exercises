#Progam liczący średnią dla n liczb
n = int(input("Podaj dla ilu liczb mam policzyć średnią: "))
suma_liczb = 0
if (n != 0):
    for i in range(n):
        liczba = int(input("Podaj " + str(i+1) + " liczbę: "))
        suma_liczb += liczba
        srednia  = suma_liczb/n
    print("średnia dla n liczb wynosi:", srednia)
else:
    print("Twoja średnia wynosi: 0",)
