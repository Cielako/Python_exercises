def szyfruj(zdanie,slownik):
    szyfr = ""
    for i in zdanie:
        a = ord(i)
        if a in slownik:#jeżeli a(numer ascii jest w słowniku), to zamień i na wartość w kodzie ascii o jeden większą
            if i == "z":
                i = chr(97)
                szyfr += i
            if i == chr(a):
                i = chr(a+1)
                szyfr+=i
        else: szyfr+=i
    return szyfr

def deszyfruj(szyfr,slownik):
    deszyfr=""
    for i in szyfr:
        a = ord(i)
        if a in slownik:#jeżeli a(numer ascii jest w słowniku), to zamień i na wartość w kodzie ascii o jeden mniejszą
            if i == "a":
                i = chr(122)
                deszyfr += i
            if i == chr(a):
                i = chr(a-1)
                deszyfr+=i
        else: deszyfr+=i
    return deszyfr

   
                