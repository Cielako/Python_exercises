def obwod(a,b,c):
    obwod = float(a + b + c)
    return obwod

def pole(a,b,c):
    from math import sqrt
    polowa_obwodu = (a + b + c)/2
    pole = float(sqrt(polowa_obwodu*(polowa_obwodu-a)*(polowa_obwodu-b)*(polowa_obwodu-c)))
    return pole

def rrr(a,b,c):#funkcja odpowiada za sprawdzenie czy trójkąt jest równoboczny, równoramienny czy równoboczny
    if a == b and a == c and b == c:
       rrr = "równoboczny !!"
       return rrr
    
    elif a == b or a == c or b == c:
        rrr = "równoramienny !!"
        return rrr
    
    else:
      rrr = "różnoramienny !!"
      return rrr 
       
def por(a,b,c):#funkcja pozwala sprawdzić czy trójkąt jest prostokątny, ostrokątny czy rozwartokątny
    if a**2+b**2 == c**2 or c**2-a**2 == b**2 or c**2-b**2 == c**2:
        por = "prostokątny !!" 
        return por
    
    elif  c**2 >= a**2 + b**2 or c**2 - b**2 >= a**2 or c**2 - a**2 >= b**2:
        por = "ostrokątny !!"
        return por
    
    elif  c**2 <= a**2 + b**2 or c**2 - b**2 <= a**2 or c**2 - a**2 <= b**2:
        por = "rozwartokątny !!"
        return por
    
