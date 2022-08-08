
# Parametric plot

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def circle():
    a=2.0
    t=np.arange(0,2*np.pi,0.01)
    x=a*np.cos(t)
    y=a*np.sin(t)
    plt.plot(x,y)
    return plt.show()
def ellipse():
    a=2.0
    b=3.0
    t=np.arange(0,2*np.pi,0.01)
    x=a*np.cos(t)
    y=b*np.sin(t)
    plt.plot(x,y)
    return plt.show()
def parabola():
    a=4.0
    t=np.linspace(-5,5,100)
    x=a*t**2
    y=2*a*t
    plt.plot(x,y)
    return plt.show()
def hyperbola():
    a=2.0
    b=1.0
    t=np.linspace(-2,2,100)
    x=a*np.cosh(t)
    y=b*np.sinh(t)
    x1=-a*np.cosh(t)
    y1=b*np.sinh(t)
    plt.plot(x,y,x1,y1)
    return plt.show()
def cylinder():
    fig=plt.figure()
    ax=fig.add_subplot(111,projection='3d')
    R=1.0
    theta=np.linspace(0,2*np.pi,50)
    z=np.linspace(0,4,50)
    z,theta=np.meshgrid(z,theta)
    x=R*np.cos(theta)
    y=R*np.sin(theta)
    ax.plot_wireframe(x,y,z)
    ax.set_xticks([-1.0,-0.5,0.0,0.5,1.0])
    ax.set_yticks([-1.0,-0.5,0.0,0.5,1.0])
    aa=ax.plot_surface(x,y,z,cmap='autumn')
    return aa,fig.colorbar(aa,shrink=0.5),plt.show()
def default():
    return "Incorrect entry"
switcher={
    1:circle,
    2:ellipse,
    3:parabola,
    4:hyperbola,
    5:cylinder,
    }
def switch(parametric):
    return switcher.get(parametric,default)()
print(switch(6))







































    
