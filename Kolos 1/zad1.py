#Program do liczenia odległości, pomiędzy dowma mpunktami (x1,y1) i (x2,y2)
from math import sqrt
x1 = float(input("Podaj współrzędną dla x1: "))
y1 = float(input("Podaj współrzędną dla y1: "))
x2 = float(input("Podaj współrzędną dla x2: "))
y2 = float(input("Podaj współrzędną dla y2: "))
odleglosc = sqrt((x1-x2)**2+(y1-y2)**2)
print("Odległość dla punktów(" + str(x1)+ " " + str(y1) + ") i (" + str(x2)+ " " + str(y2) +") wynosi: ",odleglosc)