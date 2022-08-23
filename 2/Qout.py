from cmath import pi, sqrt, tan
import numpy as np

class CalQout:
    def __init__(self,time) -> None:
        pass

    def A(h):
        """
        :param g:角度
        """
        x = 1.25 / tan(9*pi/180)
        r = 1.4 /2; R = 2.5 /2
        d = (x+h)*tan(9*pi/180)
        A0 = pi* r**2; Ah = pi*(d**2-R**2)
        return min(A0,Ah)

    def get_Qout(self,h):
        return 0.85*self.A(h)*sqrt(2*99.9/0.85)


    Hp = lambda a :  2.41*np.cos(a) + 4.85

    def Vp(self,sita):
        V0 = 20+ pi * 2.5*2.5* 4.83
        Ap = 2.5*2.5*pi
        return V0 - Ap * self.Hp(sita)