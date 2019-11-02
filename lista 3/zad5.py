import re
haslo = str(input("Podaj haslo: "))
dlugosc = len(haslo)
a = re.search("[a-z]", haslo)
b = re.search("[A-Z]", haslo)
c = re.search("[0-9]", haslo)
d = re.search("[$#@]", haslo)
if(a and b and c and d  and dlugosc >= 6 and dlugosc <= 16):
    print("Hasło jest zgodne z wymaganiami :) ")
else:{
    print("Hasło nie spełnia wymagań :( ")
}

