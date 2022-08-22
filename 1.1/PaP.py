from math import sqrt
from scipy.integrate import odeint
import numpy as np

# https://blog.csdn.net/weixin_54546190/article/details/119918657

# def caPap():
#     Pa = symbols('Pa', cls = Function) # 密度
#     Pb = symbols('Pb') # 压力
#     eq = diff(Pa(Pb),Pb)- Pa(Pb)/(0.02893 * Pb **2 + 3.077 * Pb + 1572)

#     res = dsolve(eq,Pa(Pb),ics={Pa(100):0.85})

#     print(res)
dy = lambda Pa,Pb : Pa/(0.02893 * Pb * Pb + 3.077 * Pb + 1572) # 密度/压力

x = np.arange(100,160,0.1) #压力
sol = odeint(dy,0.85,x)
print(sol)




# def cal(Pb):
#     return 0.986388509007619*exp(-0.0761510801690481*I*log(1.0*Pb + 53.1800898721051 - 226.958003650626*I) + 0.0761510801690481*I*log(1.0*Pb + 53.1800898721051 + 226.958003650626*I))

# caPap()