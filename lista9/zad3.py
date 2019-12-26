import numpy
import matplotlib.pyplot as plt

v0 = float(input("Podaj prędkość początkową w m/s: "))
alfa = float(input("Podaj kąt wyrażony za pomocą stopnii: "))

v0x = v0 * numpy.cos(alfa * numpy.pi / 180)
v0y = v0 * numpy.sin(alfa * numpy.pi / 180)
g = 9.81
vy = list()#prędkość chwilowa w kierunku pionowym po czasie t
t = list()#czas
vx = list()#prędkość chwilowa w kierunku poziomym po czasie t
Xt = list()#położenie w osi x od czasu
Yt = list()#położenie w osi y od czasu

Hmax = (v0 * numpy.sin(alfa * numpy.pi / 180))**2/(2 * g)#Maksymalna wysokość na jaką wzniesie się ciało
Z = (v0**2 * (numpy.sin((2 * alfa) * numpy.pi / 180)))/g#zasięg rzutu
Ts = (2 * v0 * numpy.sin(alfa * numpy.pi / 180))**2 / (2 * g)#Czas lotu ciała

print("Maksymalna wysokość wynosi: " + str(Hmax) + " metrów")
print("Zasięg rzutu wynosi: " + str(Z) + " metrów")
print("Czas spadania wynosi: " + str(Ts) + " sekund")

def getVy(v0x, v0y, Ts):
    for i in numpy.arange(0, Ts, 0.01):
        vy.append(v0y * numpy.sin(alfa * numpy.pi / 180)  - (g*i))
        t.append(i)
        vx.append(v0x * numpy.cos(alfa * numpy.pi / 180))

def getXt(v0x, Ts):
    for i in numpy.arange(0, Ts, 0.01):
       Xt.append(v0x * i * numpy.cos(alfa * numpy.pi / 180))

def getYt(v0y, Ts):
    for i in numpy.arange(0, Ts, 0.01):
        Yt.append((v0y * i * numpy.sin(alfa * numpy.pi / 180))  - (g*(i**2)) / 2)

fig, (w1, w21, w22, w3) = plt.subplots(4)

getVy(v0x, v0y, Ts)
getXt(v0x, Ts)
getYt(v0y, Ts)
w1.plot(t, vy)
w21.plot(t, vx)
w22.plot(Xt, t)
w3.plot(Xt, Yt)
plt.show()