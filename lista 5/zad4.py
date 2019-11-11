klucz = {"a":"y","e":"i","i":"o","o":"a","y":"e"}
odwrocony_klucz = dict(map(reversed, klucz.items()))#umożliwia odwrócenie klucza szyfrującego
def deszyfruj(slowo):
    for item in slowo:
        for key, value in odwrocony_klucz.items():
            if item in key:
                slowo = slowo.replace(key,value)
    print (slowo)
    
def szyfruj():
    slowo = input("Podaj jakis wyraz: ")
    for item in slowo:
        for key, value in klucz.items():
            if item in key:
                slowo = slowo.replace(key,value)
    print (slowo)
    deszyfruj(slowo)
szyfruj()