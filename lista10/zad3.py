from itertools import combinations

class Suma:
    def __init__(self,lista):
       self.lista = lista
       
    def podlisty(self):
        podlisty = []
        
        for i in range(0, len(self.lista) + 1):
            podlista = [list(x) for x in combinations(self.lista,i) if len(x) == 3 and sum(x) == 0]
            podlisty.extend(podlista)
        return podlisty
    
NowaLista = Suma([0,-1,1,2,-2])
print("Podlista:", NowaLista.podlisty())