with open('./2/inin.txt','r') as f:
    res = f.readlines()
    x,y=[],[]
    for i in res:
        [ key, value ] = i.replace('\n','').split('\t') 
        x.append(float(key))
        y.append(float(value))
    
from cmath import cos, pi
import matplotlib.pyplot as plt
import numpy as np

x = np.array(x)
y = np.array(y)

fit_x = np.linspace(0,2*pi,1000)
fit_y = 2.41*np.cos(fit_x) + 4.85

plt.scatter(x,y,c='g')
plt.plot(fit_x,fit_y)
plt.show()