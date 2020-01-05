import numpy as np
class Kolo:
    def __init__(self, r):
        self.promien = r
        
    def pole(self):
        wynik = np.pi * (self.promien ** 2)
        return wynik
     
    def obwod(self):
        wynik = 2 * np.pi * self.promien
        return wynik

NoweKolo = Kolo(8)
print("Pole koła wynosi:",NoweKolo.pole())
print("Obwód koła wynosi:",NoweKolo.obwod())
