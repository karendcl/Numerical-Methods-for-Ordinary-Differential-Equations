import numpy as np

def Divide(start ,h, end):
    x = [start]

    while(start < end):
        start += h
        a = round(start,3)
        x.append(a)
    
    return x
    return np.linspace(0, end, int(end/h))

def MtodoEuler(x0,y0,h,f):
    for i in range(1,len(x0)):
        xn = x0[i-1]
        yn = y0[i-1]
        y0.append(xn + h*f(xn,yn))
    
        a = y0[i]
        b = complex(a).real
        c = round(b,3)
        y0[i]= c

def MetodoEulerMejor(x0,y0,h,f):
    for i in range(0,len(x0)-1):
        k1 = f(x0[i],y0[i])
        u= y0[i]+h*k1
        k2=f(x0[i+1],u)
        y0.append(y0[i] + h/2*(k1+k2))
        y0[i+1]= round(y0[i+1],3)
        
def MetodoRunge_Kutta(x0,y0,h,f):
    for i in range(0,len(x0)-1):
        k1= f(x0[i],y0[i])
        k2= f(x0[i]+ h/2, y0[i]+h*k1/2 )
        k3= f(x0[i]+ h/2, y0[i]+h*k2/2 )
        k4= f(x0[i+1], y0[i]+ h*k3)
        y0.append(y0[i]+  h/6 *(k1+2*k2+2*k3+k4))
        y0[i+1]= round(y0[i+1],3)
 
    

    
    



