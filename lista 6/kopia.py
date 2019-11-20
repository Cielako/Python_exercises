def szyfruj(zdanie,slownik):
    for i in zdanie:
        for a in slownik:
            if i == "z":
                a = slownik[0]
                zdanie = zdanie.replace(i,chr(a))
            elif i == chr(a):
                zdanie = zdanie.replace(i,chr(a+1))
            
    return zdanie
                