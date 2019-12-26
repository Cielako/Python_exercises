import sys,numpy
def pobierzArg(arg):
    argumenty = list()
    argumenty = [int(x) for x in arg.split(',')]
    return argumenty
#print(pobierzArg(sys.argv[1]))----Sprawdzenie czy funkcja działa
#sys.argv[1]-argument wejściowy w tym przypadku to string  

def pobierzArg_plik(arg):
    argumenty = list()
    plik = open("dane.txt","r").read()
    argumenty = [int(x) for x in plik.split(',')]
    return argumenty
#print(pobierzArg_plik(sys.argv[1]))----Sprawdzenie czy funkcja działa
    
def statystyka(arg):
    print("Średnia:",numpy.average(arg))
    print("Wariancja:",numpy.var(arg))
    print("Odchylenie standardowe:",numpy.std(arg))

if "dane.txt" in sys.argv[1]:
    statystyka(pobierzArg_plik(sys.argv[1]))
else: 
    statystyka(pobierzArg(sys.argv[1]))