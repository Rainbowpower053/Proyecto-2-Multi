from random import random, seed, uniform
from numpy import exp, sin, cos, pi


def fmat(a, b, c): 
    val = (exp(-(a**2)*sin(b*2*pi)*sin(c*(pi/2))*cos(c*(pi/2))))*((a**2)*sin(c*(pi/2))*(pi**2))
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
        w = fmat(lista_puntos[i][0], lista_puntos[i][1], lista_puntos[i][2])
        suma += w

    valor_final = suma / num
    return valor_final

print(monte_carlo(100000))