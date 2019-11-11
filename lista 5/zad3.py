def rzymskie_dziesietne():
    rzymskie = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    dziesietne = 0
    liczba = (input("Podaj liczbę w formacie rzymskim:")).upper()
    for i in range(len(liczba)):
        if i > 0 and rzymskie[liczba[i]] > rzymskie[liczba[i-1]]:
            dziesietne += rzymskie[liczba[i]]-2*rzymskie[liczba[i-1]]
        else: dziesietne += rzymskie[liczba[i]]
    print(dziesietne)
            
rzymskie_dziesietne()