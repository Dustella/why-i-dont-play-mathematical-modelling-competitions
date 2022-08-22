

from math import pi, sqrt
import numpy as np


Ap = 2.5*2.5*pi

class CalQin:
    res = []
    wr = 0
    E = lambda a:a
    ranging = 1* 1000* 100

    def __init__(self,wr) -> None:
        self.wr = wr /(1000*100)
        for i in range(self.ranging):
            self.interation()

    def qr(self,Pr_last):
        if Pr_last < 100 : return 0
        return 0.85* Ap *sqrt(2*(Pr_last-100)/0.85) 

    def Vp(self,sita):
        vmax = 20 + Ap *4.82
        vip =  Ap*(2.41*np.cos(sita) + 4.85)
        return vmax -vip

    def interation(self):
        if len(self.res) == 0:
            Pr_last = 0.5
        else:
            Pr_last = self.res[-1]

        time = len(self.res) / 100
        sita = self.wr * time + pi

        E =  3.077 * Pr_last + 1572
        v= self.Vp(sita)
        d_Pr_this_tick = E*(-Ap *2.41* np.sin(sita)*0.01 - self.qr(Pr_last))/v
        print(f"sita {sita}, Prlast {Pr_last}, time {time}ms, qr{self.qr(Pr_last)}")
        # import time 
        # time.sleep(0.00001)
        self.res.append(Pr_last+ d_Pr_this_tick)

if __name__ == "__main__":
    test = CalQin(620)
    res  =  test.res
    import matplotlib.pyplot as plt
    import numpy as np
    x = np.linspace(0,10000,len(res))
    plt.plot(x,res)
    plt.show()