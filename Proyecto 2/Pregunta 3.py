from random import random, seed, uniform
from numpy import exp, sin, cos, pi

seed(11)

def fmat(r, t, p): 
    val = (exp(-(r)*sin(t*pi/2)*sin(p*(pi**2))*cos(p*(pi**2))))*((r**2)*sin(p*(pi**2)))
    return val
    
def monte_carlo(num):
    lista_puntos = [] 
    for i in range(num): 
        r = uniform(0, 1)
        t = uniform(0, 1)
        p = uniform(0, 1)
        lista_puntos.append([r,t,p])
    
    suma = 0
    for i in range(num): 
        w = fmat(r, t, p)
        suma += w

    valor_final = suma / num
    return valor_final

print(monte_carlo(100000))