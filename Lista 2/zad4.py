napis = input("Wczytaj jakiś napis: ")
lp = napis[0]
zmieniony = napis[1:].replace(lp,"$")
print (lp + zmieniony)
