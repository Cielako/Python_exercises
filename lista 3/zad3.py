import sys
from math import sqrt
a = float(input("Podaj a: "))
while(a<=0):
    a = float(input("Podaj ponownie współczynnik a, żeby równanie było kwadratowe: ")) 
b = float(input("Podaj b: "))
c = float(input("Podaj c: "))
delta = (b**2)-(4*a*c)
if(delta < 0):
    print("To równanie kwadratowe nie ma rozwiązań !!!")
    sys.exit()
else: 
    x1 = (-b-sqrt(delta))/(2*a)
    x2 = (-b+sqrt(delta))/(2*a)
print("x1 jest równe: ",x1," x2 jest równe: ",x2)
    


