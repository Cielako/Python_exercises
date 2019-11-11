def zamien():
    slownik = {"1":"jeden", "2":"dwa","3":"trzy","4":"cztery","5":"pięć", "6":"sześć","7":"siedem","8":"osiem","9":"dziewięć","10":"dziesięć"}
    liczba = input("Podaj liczbę w postaci cyfr(zakres od 1 do 1999): ")
    dziesietne=""
    for i in range(len(liczba)):
        if i > 0 and slownik[liczba[i]] > slownik[liczba[i-1]]:
            dziesietne += slownik[liczba[i]]-2*slownik[liczba[i-1]]
        else: dziesietne += slownik[liczba[i]]
    print(dziesietne)
zamien()