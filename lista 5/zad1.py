def zamien():
    slownik = {"jeden":1, "dwa":2, "trzy":3, "cztery":4, "pięć":5, "sześć":6, "siedem":7, 
    "osiem":8, "dziewięć":9,"dziesięć":10, "jedenaście":11, "dwanaście":12, "trzynaście":13, "czternaście":14,"piętnaście":15, "szesnaście":16, "siedemnaście":17, "osiemnaście":18, "dziewiętnaście":19,
    "dwadzieścia":20, "trzydzieści":30, "czterdzieści":40, "pięćdziesiąt":50}
    liczba_slownie = input("Podaj liczbę (słownie z zakresu od 1 do 59): ")
    rozdziel = liczba_slownie.split() #ignoruje spację pomiędzy stringami i tworzy tablicę
    for i in range(len(rozdziel)):
        if i == 0:
            x = slownik[rozdziel[i]]
        if i == 1:
            x += slownik[rozdziel[i]]
            print("Twoja Liczba to:",x)
zamien()