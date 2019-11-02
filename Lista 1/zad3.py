import math
a= float(input("Podaj dlugosc 1 boku: "))
b= float(input("Podaj dlugosc 2 boku: "))
alpha = math.radians(float(input("Podaj kąt w stopniach: ")))
pole = a*b*0.5*math.sin(alpha)
print(pole)