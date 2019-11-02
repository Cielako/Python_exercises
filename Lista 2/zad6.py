lista = ["Kasia","Basia","Marek","Darek"]
lista.append("Józek")
lista.extend(["Ania","Basia"])
posortowani = sorted(lista)
print("Posortowana lista: ",posortowani)
print("Czwarta osoba z listy to: ",posortowani[3])
print("Dwie pierwsze osoby na liście to: ",posortowani[0:2])
print("Dwie ostatnie osoby na liście to: ",posortowani[5:7])
while "Basia" in posortowani: posortowani.remove("Basia")
print ("Lista bez Basi: ",posortowani)
print ("Ilość studentów wynosi: ",len(posortowani))
krotka = (posortowani[0:])
print("Krotka wygląda następująco: ",krotka)



