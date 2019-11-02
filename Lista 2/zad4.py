napis = input("Wczytaj jakiś napis: ")
x=float(len(napis))
for x,element in enumerate(napis):
    if element==napis[0]:
        napis[x] = "$"
print(napis)
#napis = napis.replace(napis[0],"$")
