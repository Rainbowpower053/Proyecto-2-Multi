from random import random, seed, uniform
from sympy import symbols
from numpy import sqrt, pi, cos, sin
from scipy import integrate

seed(11) #El comando random.seed() hace que se generen de manera aleatoria los mismos números. Solo se hizo para mantener un orden en la resolución del ejercicio.

#Esta función de Python es para uno ingresar la función que quiere estudiar. En el caso de la pregunta 2, sería la función f(x,y) = xy^2.
def fmat(x,y): #Los parámetros a ingresar son las variables de estudio, en nuestro caso, nosotros utilizamos las variables x e y.
    val = (pi/2)*(x**4)*cos((pi/4)+(y*pi/2))*(sin((pi/4)+(y*pi/2)))**2
    return val #Lo que retorna la función es la expresión de esta, para verla en forma general (es decir, con variables en vés de números), se requiere especificar las variables
               #Mediante el comando sympy.symbols.

#Esta función de Python es la resolución del Método de Monte Carlo.
def monte_carlo(num): #El parámetro a ingresar es la cantidad de iteraciones.
    lista_puntos = [] #En esta lista se guardan los puntos generados por el comando random.random() <- Este comando genera números reales entre 0 y 1.
    for i in range(num): #Este ciclo for es para generar puntos num cantidad de veces, es decir vamos a generar una cantidad de puntos igual al número de iteraciones.
        x = uniform(0, 1) #Con el comando random.uniform(a, b), se generan números entre a y b, que en el contexto de la pregunta, sería entre 0 y 1.
        y = uniform(0, 1) #Lo mismo que la variable x.
        lista_puntos.append([x,y]) #Con este comando, nosotros guardamos los valores generados seudo aleatoriamente (por el comando random.seed()) en una lista que se utilizará para
        #evaluar la función.

    suma = 0 
    for i in range(num): #Con este ciclo for, nostros vamos sumando los valores de las imagenes de las variables. Se utiliza la variable sum que sirve para ir acumulando los valores y la 
        #z que es es la función evaluada por los valores de x e y.
        z = fmat(x, y)
        suma += z #Con este ccomando vamos acumlando los valores de z.

    valor_final = suma/num #Esta variable es la aproximación del volumen de la función mediante el Método de Monte Carlo. Es importante destacar que el valor de (b-a) es 1.
    return valor_final

x,y = symbols("x,y")
f = lambda y, x: (pi/2)*(x**4)*cos((pi/4)+(y*pi/2))*(sin((pi/4)+(y*pi/2)))**2
I = integrate.dblquad(f, 0, 1, lambda x: 0, lambda x: 1)
print(f"Con la función scipy.integrate.dblquad retorna el valor de la integral doble de la función y un estimado del error del cálculo. {I}")
print("Entonces el resultado de la integral de la segunda pregunta es 3.89E18, con un error de 4.74E-15.")
print(f"El valor de la integral doble es {monte_carlo(10)} cuando el número de iteraciones N es 10.")
print(f"El valor de la integral doble es {monte_carlo(50)} cuando el número de iteraciones N es 50.")
print(f"El valor de la integral doble es {monte_carlo(100)} cuando el número de iteraciones N es 100.")
print(f"El valor de la integral doble es {monte_carlo(500)} cuando el número de iteraciones N es 500.")
print(f"El valor de la integral doble es {monte_carlo(1000)} cuando el número de iteraciones N es 1000.")
print(f"El valor de la integral doble es {monte_carlo(5000)} cuando el número de iteraciones N es 5000.")
print(f"El valor de la integral doble es {monte_carlo(10000)} cuando el número de iteraciones N es 10000.")
print(f"El valor de la integral doble es {monte_carlo(50000)} cuando el número de iteraciones N es 50000.")
print(f"El valor de la integral doble es {monte_carlo(100000)} cuando el número de iteraciones N es 100000.")
print(f"El valor de la integral doble es {monte_carlo(500000)} cuando el número de iteraciones N es 500000.")