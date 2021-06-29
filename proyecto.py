import numpy as np
import math as m
#CONDICIONES INICIALES
vo = np.array([1,0],dtype = float)
g = 9.8#m/s**2
m1 = 2.0#kg
m2 = 3.0#kg
lon1 = 4.0#cm
lon2 = 2.0#cm
#VARIABLES INICIALES
x1,x2,x3,x4 = 0
ao,bo,yo,go = 0
a = ao
b = bo
y = yo
g = go

#FUNCIONES DEL PENDULO
def l(dt,x1,x2,x3,x4):
    a = 0
    return a
    
def mm(dt,x1,x2,x3,x4):
    a = 0
    return a
def n(dt,x1,x2,x3,x4):
    a = 0
    return a
def o(dt,x1,x2,x3,x4):
    a = 0
    return a


#RK4 SEGÚN EL PROFE
def rk4(N,a,b,y,g):
    v = vo
    t = 0
    dt = 0.2
    for i in range(N):
        l1 = l(t,a,b,y,g)
        l2 = l(t + dt/2,a+((dt*l1)/2),b +((m1*dt)/2),y +((n1*dt)/2),y +((o1*dt)/2))
        l3 = l(t + dt/2,a+((dt*l2)/2),b +((m2*dt)/2),y +((n2*dt)/2),y +((o2*dt)/2))
        l4 = l(t + dt/2,a+((dt*l3)/2),b +((m3*dt)/2),y +((n3*dt)/2),y +((o3*dt)/2))

        m1 = mm(t,a,b,y,g)
        m2 = mm(t + dt/2,a+((dt*l1)/2),b +((m1*dt)/2),y +((n1*dt)/2),y +((o1*dt)/2))
        m3 = mm(t + dt/2,a+((dt*l2)/2),b +((m2*dt)/2),y +((n2*dt)/2),y +((o2*dt)/2))
        m4 = mm(t + dt/2,a+((dt*l3)/2),b +((m3*dt)/2),y +((n3*dt)/2),y +((o3*dt)/2))

        n1 = n(t,a,b,y,g)
        n2 = n(t + dt/2,a+((dt*l1)/2),b +((m1*dt)/2),y +((n1*dt)/2),y +((o1*dt)/2))
        n3 = n(t + dt/2,a+((dt*l2)/2),b +((m2*dt)/2),y +((n2*dt)/2),y +((o2*dt)/2))
        n4 = n(t + dt/2,a+((dt*l3)/2),b +((m3*dt)/2),y +((n3*dt)/2),y +((o3*dt)/2))
        
        o1 = o(t,a,b,y,g)
        o2 = o(t + dt/2,a+((dt*l1)/2),b +((m1*dt)/2),y +((n1*dt)/2),y +((o1*dt)/2))
        o3 = o(t + dt/2,a+((dt*l2)/2),b +((m2*dt)/2),y +((n2*dt)/2),y +((o2*dt)/2))
        o4 = o(t + dt/2,a+((dt*l3)/2),b +((m3*dt)/2),y +((n3*dt)/2),y +((o3*dt)/2))

        a += dt/6*(l1+2*l2+2*l3+l4)
        b += dt/6*(m1+2*m2+2*m3+m4)
        y += dt/6*(n1+2*n2+2*n3+n4)
        g += dt/6*(o1+2*o2+2*o3+o4)

        

    
    
