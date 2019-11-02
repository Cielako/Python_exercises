print("Program wygeneruje dwuwymiarową tablicę ")
m = int(input("Podaj pierwszą liczbę (wierszy w tablicy): "))
n = int(input("Podaj drugą liczbę (kolumn w tablicy): "))
tablica = [[0 for i in range(n)] for j in range(m)]
for i in range(m):
    for j in range(n):
        tablica[i][j]=i*j
print (tablica)