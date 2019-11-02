n = int(input("Podaj n-ty wyraz ciągu, dla którego mam wyznaczyć wartość: "))
#a = int(input("Podaj pierwszy wyraz ciągu: ")) #Po odkomentowaniu tych dwóch zmiennych,  
#q = int(input("Podaj iloraz ciągu: ")) # oraz zmianie 1 na a i 2 na q w wywołaniu funkcji możemy wtedy policzyć  n-ty wyraz ciągu dla dowolnej wartosci pierwszego elementu i ilorazu ciągu
def ciag(n,a,q):
    wyraz_n = a*(q**(n-1))
    print("Wartośc",n,"-ego wyrazu ciągu geometrycznego wynosi: ",wyraz_n)
ciag(n,1,2)