from SzyfrCezara import *
slownik = [97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122]
zdanie = str(input("Podaj jakieś zdanie testowe: "))
print("Zakodowane zdanie brzmi:",szyfruj(zdanie,slownik))
print("Rozkodowane zdanie brzmi:",deszyfruj(szyfruj(zdanie,slownik),slownik))