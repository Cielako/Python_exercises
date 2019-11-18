from zad1 import boki

def obwod(obwod):
    obwod = float(boki[0] + boki[1] + boki[2])
    return obwod

def pole(pole):
    from math import sqrt
    polowa_obwodu = (boki[0] + boki[1] + boki[2])/2
    pole = float(sqrt(polowa_obwodu*(polowa_obwodu-boki[0])*(polowa_obwodu-boki[1])*(polowa_obwodu-boki[2])))
    return pole

def rrr(rrr):#funkcja odpowiada za sprawdzenie czy trójkąt jest równoboczny, równoramienny czy równoboczny
    if boki[0] == boki[1] and boki[0] == boki[2] and boki[1] == boki[2]:
       rrr = "równoboczny !!"
       return rrr
    
    elif boki[0] == boki[1] or boki[0] == boki[2] or boki[1] == boki[2]:
        rrr = "równoramienny !!"
        return rrr
    
    else:
      rrr = "różnoramienny !!"
      return rrr 
       
def por(por):#funkcja pozwala sprawdzić czy trójkąt jest prostokątny, ostrokątny czy rozwartokątny
    if boki[0]**2+boki[1]**2 == boki[2]**2 or boki[2]**2-boki[0]**2 == boki[1]**2 or boki[2]**2-boki[1]**2 == boki[0]**2:
        por = "prostokątny !!" 
        return por
    
    elif  boki[2]**2 >= boki[0]**2 + boki[1]**2 or boki[2]**2 - boki[1]**2 >= boki[0]**2 or boki[2]**2 - boki[0]**2 >= boki[1]**2:
        por = "ostrokątny !!"
        return por
    
    elif  boki[2]**2 <= boki[0]**2 + boki[1]**2 or boki[2]**2 - boki[1]**2 <= boki[0]**2 or boki[2]**2 - boki[0]**2 <= boki[1]**2:
        por = "rozwartokątny !!"
        return por
    
print("Obwód tego trójkąta wynosi:",obwod(obwod))
print("Pole tego trojkata wynosi:",pole(pole))
print("Ten trójkąt jest " + rrr(rrr))
print("Ten trójkąt jest " + por(por))