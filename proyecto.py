import numpy as np
import math as m
#CONDICIONES INICIALES
g = 9.8#m/s**2
m1 = 2.0#kg
m2 = 3.0#kg
t = 0
lon1 = 4.0#cm
lon2 = 2.0#cm
#VARIABLES INICIALES
#es necesario darle valores iniciales  con los valores iniciales de cada uno
x1 = 1
x2 = 0
x3 = 1
x4 = 0


#FUNCIONES DEL PENDULO

def l(dt,x1,x2,x3,x4):
    """
    l = theta prima  = x2
    """
    lRespuesta = x2 
    return lRespuesta
    
def mm(dt,x1,x2,x3,x4):
    """
    se definio como mm porque m se usa para la libreria .math
    """
    mArriba = ( -g*(2*m1 + m2)*m.sin(x1-2*x3) - m2*g*m.sin(x1-2*x3)-2*m.sin(x1-x3)*m2*(pow(x4,2)*lon2+pow(x2,2)*lon1*m.cos(x1-x3)) )
    mAbajo = lon1*(2*m1 + m2 -m2*m.cos(2*x1-2*x3))
    mResultado = mArriba/mAbajo
    return mResultado
def n(dt,x1,x2,x3,x4):
    """
    n = theta 2 prima  = x4
    """
    nRespuesta = x4
    return nRespuesta

def o(dt,x1,x2,x3,x4):
    oArriba = 2*m.sin(x1-x3)*(pow(x2,2)*lon1*(m1+m2)+g*(m1+m2)*m.cos(x1)+pow(x4,2)*lon2*m2*m.cos(x1-x3))
    oAbajo  = lon2*(2*m1+m2 -m2*m.cos(2*x1-2*x3))
    oRespuesta = oArriba/oAbajo
    return oRespuesta

#valores de la función iniciales
a = l(t,x1,x2,x3,x4)
b = mm(t,x1,x2,x3,x4)
y = n(t,x1,x2,x3,x4)
g = o(t,x1,x2,x3,x4)
#RK4 SEGÚN EL PROFE
def rk4(N,a,b,y,g):  
    dt = 0.2
    for i in range(N):
        l1 = l(t,a,b,y,g)
        mm1 = mm(t,a,b,y,g)
        n1 = n(t,a,b,y,g)
        o1 = o(t,a,b,y,g)

        l2 = l(t + dt/2,a+((dt*l1)/2),b +((mm1*dt)/2),y +((n1*dt)/2),g +((o1*dt)/2))
        mm2 = mm(t + dt/2,a+((dt*l1)/2),b +((mm1*dt)/2),y +((n1*dt)/2),g +((o1*dt)/2))
        n2 = n(t + dt/2,a+((dt*l1)/2),b +((mm1*dt)/2),y +((n1*dt)/2),g +((o1*dt)/2))
        o2 = o(t + dt/2,a+((dt*l1)/2),b +((mm1*dt)/2),y +((n1*dt)/2),g +((o1*dt)/2))

        l3 = l(t + dt/2,a+((dt*l2)/2),b +((mm2*dt)/2),y +((n2*dt)/2),g +((o2*dt)/2))
        mm3 = mm(t + dt/2,a+((dt*l2)/2),b +((mm2*dt)/2),y +((n2*dt)/2),g +((o2*dt)/2))
        n3 = n(t + dt/2,a+((dt*l2)/2),b +((mm2*dt)/2),y +((n2*dt)/2),g +((o2*dt)/2))
        o3 = o(t + dt/2,a+((dt*l2)/2),b +((mm2*dt)/2),y +((n2*dt)/2),g +((o2*dt)/2))

        l4 = l(t + dt,a+((dt*l3)),b +((mm3*dt)),y +((n3*dt)),g +((o3*dt)))
        mm4 = mm(t + dt,a+((dt*l3)),b +((mm3*dt)),y +((n3*dt)),g +((o3*dt)))
        n4 = n(t + dt,a+((dt*l3)),b +((mm3*dt)),y +((n3*dt)),g +((o3*dt)))
        o4 = o(t + dt,a+((dt*l3)),b +((mm3*dt)),y +((n3*dt)),g +((o3*dt)))

        a += dt/6*(l1+2*l2+2*l3+l4)
        b += dt/6*(mm1+2*mm2+2*mm3+mm4)
        y += dt/6*(n1+2*n2+2*n3+n4)
        g += dt/6*(o1+2*o2+2*o3+o4)
        print(a," ",b," ",y," ",g)
rk4(10, a,b,y,g)
        

    
    
