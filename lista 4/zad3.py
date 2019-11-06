from math import radians,degrees
def radiany(stopnie):
    print("Wartość w radianach wynosi: ",radians(stopnie))
def stopnie(radiany):
    print("Ilość stopni wynosi: ",degrees(radiany))

opcja = int(input("Wybierz opcję(1-stopnie na radiany 2-radiany na stopnie): "))

if opcja == 1:
    stopnie = int(input("Podaj stopnie: "))
    radiany(stopnie)

if opcja == 2:
    radiany = float(input("Podaj wartość w radianach: "))
    stopnie(radiany)
