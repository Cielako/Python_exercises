import time
n = int(input("do którego elementu ciągu fibonnaciego mam wypisać zaczynając od 0: "))
def iteracyjna(n):
    czas = time.time()
    a, b = 0, 1
    print("1 :", a)
    print("2 :", b)
    for i in range(1, n - 1):
        # wynik = a + b
        a, b = b, a + b
        print( str(i + 2)+" :", b)
    print("Czas mojej aplikacji zajął:",time.time()-czas)
    
print("-----------")
def rekurencyjna(n):
    czas = time.time()      
    def obliczenia(n):
        if n == 1:
            return 0
        elif n == 2:
            return 1
        elif n > 2 :
            return obliczenia(n-1) + obliczenia(n-2)
    for i in range(1,n+1):
        print (i, ':', obliczenia(i))
    print("Czas mojej aplikacji zajął:",time.time()-czas)

iteracyjna(n)
rekurencyjna(n)
#jak można zauważyć iteracyjny ciąg fibonacciego wykonał się dużo szybciej dla np.35 niż poprzez rekurencję
