from math import degrees,atan #atan służy do zamiany na radiany
from cmath import phase # zaimportowanie funkcji sprzężenia
re= float(input("Podaj część rzeczywsitą liczby zespolonej: "))
im = float(input("Podaj część urojoną liczby zespolonej: "))
z = complex(re,im)
modul = abs(z)#abs() pozwala wyznaczyc wartość bezwzględną
print ("Wartość bezwzględna z liczby zespolonej(z) wynosi: ", modul)
rad = atan(re/im)# zeby wyznaczyc radiany dzielimy część rzeczywistą przez urojoną
print("Argument w radianach wynosi: ",rad)
stp = degrees(rad)
print("Argument w stopniach wynosi: ",stp)

print("Sprzężenie jest równe: ",phase(z))