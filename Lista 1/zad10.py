import cmath
z= 1j
sinus = cmath.sin(z)
cosinus = cmath.cos(z)
print("Część rzeczywista dla sin(z) wynosi: ",sinus.real)
print("Część urojona dla sin(z) wynosi: ",sinus.imag)
print("Część rzeczywista dla cos(z) wynosi: ",cosinus.real)
print("Część urojona dla cos(z) wynosi: ",cosinus.imag)
print("zależność nie jest spełniona, ponieważ wynik wynosi: ",cmath.sin(z)**2+cmath.cos(z)**2)#zależność nie jest spełniona, ponieważ wynik wynosi 1.0000000000000002 + 0 j