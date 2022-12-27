from cProfile import label
from wsgiref import headers
import TareaEDOMetodos as EDO
from cmath import e, log
import matplotlib.pyplot as plt
from tabulate import tabulate
import numpy as np

h =0.05

start = 0
end = 50
condinicial = 0.1

def Funcion(t,N):
    return 0.1 * N * log(1/N).real -  0.1 * N


x0 = []
x0.append(start)
x0.extend(EDO.Divide(start,h,end))
yEuler = []
yEulerMejorado = []
yRunge_Kutta =[]

yEuler.append(condinicial)
yEulerMejorado.append(condinicial)
yRunge_Kutta.append(condinicial)

    

EDO.MtodoEuler(x0,yEuler,h,Funcion)
EDO.MetodoEulerMejor(x0,yEulerMejorado,h,Funcion)
EDO.MetodoRunge_Kutta(x0,yRunge_Kutta,h,Funcion)




#table = [x, y]
#print(tabulate(table, headers="firstrow"))

print(len(x0))

plt.plot(x0,yEulerMejorado, label = 'Aproximacion Euler Mejorado')
plt.plot(x0,yEuler, label = 'Aproximacion Euler')
plt.plot(x0,yRunge_Kutta, label = 'Aproximacion Runge-Kutta')
plt.legend()
plt.show()



