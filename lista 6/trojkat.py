from zad1 import boki

def obwod():
    obwod = float(boki[0] + boki[1] + boki[2])
    print("Obwod tego trojkata wynosi:",obwod)

def pole():
    from math import sqrt
    polowa_obwodu = (boki[0] + boki[1] + boki[2])/2
    pole = float(sqrt(polowa_obwodu*(polowa_obwodu-boki[0])*(polowa_obwodu-boki[1])*(polowa_obwodu-boki[2])))
    print("Pole tego trojkata wynosi:",pole)

def rrr():#funkcja odpowiada za sprawdzenie czy trójkąt jest równoboczny, równoramienny czy równoboczny
    if boki[0] == boki[1] and boki[0] == boki[2] and boki[1] == boki[2]:
       print("Ten trójkąt jest równoboczny !!")
    
    elif boki[0] == boki[1] or boki[0] == boki[2] or boki[1] == boki[2]:
       print("Ten trójkąt jest równoramienny !!")
    
    else:
       print("Ten trójkąt jest różnoramienny !!") 
       
def por():#funkcja pozwala sprawdzić czy trójkąt jest prostokątny, ostrokątny czy rozwartokątny
    if boki[0]**2+boki[1]**2 == boki[2]**2 or boki[2]**2-boki[0]**2 == boki[1]**2 or boki[2]**2-boki[1]**2 == boki[0]**2:
        print("Ten trójkąt jest prostokątny !!") 
    elif  boki[2]**2 >= boki[0]**2 + boki[1]**2 or boki[2]**2 - boki[1]**2 >= boki[0]**2 or boki[2]**2 - boki[0]**2 >= boki[1]**2:
        print("Ten Trójkąt jest ostrokątny !!")
    elif  boki[2]**2 <= boki[0]**2 + boki[1]**2 or boki[2]**2 - boki[1]**2 <= boki[0]**2 or boki[2]**2 - boki[0]**2 <= boki[1]**2:
        print("Ten Trójkąt jest rozwartokątny !!")
obwod()
pole()
rrr()
por()