from itertools import combinations
class Lista:    
    def __init__(self,lista):
        self.lista = lista
        
    def podlisty(self):
        podlisty = []
        
        for i in range(0, len(self.lista) + 1):
            podlista = [list(x) for x in combinations(self.lista,i)]
            
            if len(podlista) < 0:
                return -1
            else:
                podlisty.extend(podlista)
        return podlisty
                

NowaLista = Lista([1,2,3])
print("Podlisty:", NowaLista.podlisty())
                