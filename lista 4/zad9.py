n=int(input("Podaj liczbę całkowitą (dodatnią), dla której mam policzyć silnię: "))#pobieram liczbę dla której mam wypisać silnię
def program_silnia(n):
    liczba = n+1#zwiększam o 1 dla pętli z range
    if n == 1:
        print("Silnia z Twojej liczby to: ",n)
    elif n < 1:
        print("Nie jestem w stanie policzyć z tej liczby silnii !")
    else:
        silnia=1
        for a in range(1,liczba):
            silnia*=a
    print("Silnia dla liczby ",n," wynosi: ",silnia)
program_silnia(n)