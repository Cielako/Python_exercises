from math import degrees
r = int(input("Podaj wartość Parametru R: "))
g = int(input("Podaj wartość Parametru G: "))
b = int(input("Podaj wartość Parametru B: "))
def RGB_na_HSV(r,g,b):
    r_prim = r/255.0
    g_prim = g/255.0
    b_prim = b/255.0
    Cmax = max(r_prim,b_prim,g_prim)
    Cmin = min(r_prim,b_prim,g_prim)
    delta = Cmax - Cmin
    if delta == 0:
        h = 0
    elif Cmax == r_prim:
        h =(60 * ((g_prim-b_prim)/delta) + 360) % 360
    elif Cmax == g_prim:
        h =(60 * ((b_prim-r_prim)/delta) + 120) % 360
    elif Cmax == b_prim:
        h =(60 * ((r_prim-g_prim)/delta) + 240) % 360
    if Cmax == 0:
        s = 0
    else:
        s = (delta/Cmax)*100
    v =  Cmax*100
    print("Po konwersji z RGB, wartość HSV wynosi:",h,s,v)
RGB_na_HSV(r,g,b)
    
