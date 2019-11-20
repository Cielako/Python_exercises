n = int(input("Podaj liczbę(n) dla której mam wypisać n pierwszych wyrazów ciągu look-and-say: "))
def look_n_say(s):
    wynik = []
    i = 0
    while i < len(s):
        count = 1
        while i + 1 < len(s) and s[i] == s[i+1]:
            i += 1
            count += 1
        wynik.append(str(count) +s[i])
        i += 1
    return ''.join(wynik)
s="1"
for i in range(n):
    s = look_n_say(s)
    print(s)
