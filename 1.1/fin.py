"""
author: Dustella
description: 
第一题计算最佳阀门打开时间
"""
import matplotlib.pyplot as plt
# 约定：所有时间以ms为单位，从0开始
from math import sqrt
import numpy as np

class Generator:
    Qin_at_160 = 0.7 * 0.7 * 3.14 * 0.85*sqrt(2*60/0.87099033) # 压力160时进油量
    # 设置传入的打开时间
    duration = 0 # 传入的阀门打开时间
    Pr_full = [] # 记录每0.01ms的管内压
    ranging = 10 * 1000 * 100

    def __init__(self, duration) -> None:
        """对于一个打开毫秒，计算差平方的和
        args:
            - duration 阀门打开时间
        """
        self.Pr_full = [] # 重置整个状态
        self.duration = duration
        for i in range(self.ranging):
            self.iteration()


    def get_Qin(self, time):
        """
        对于一个确定的时间，得到这个时间的Qin
        """
        offset = time % (self.duration+10)
        if offset > self.duration:
            return 0
        return self.Qin_at_160*0.01

    def get_Qout(self,time):
        """对于一个确定的时间，得到这个时间段Qout"""
        offset = time % 100 - 50
        if abs(offset) < 48.8 :
            return 0
        if abs(offset) > 1:
            return 20 * 0.01
        return (100*abs(offset)-4880)*0.01

    # 主要函数，用来迭代
    def iteration(self):
        """Pr_last:上一秒钟的Pr压力"""

        if len(self.Pr_full) == 0:
            Pr_last = 160
        else:
            Pr_last = self.Pr_full[-1]
        v = 500 * 3.14 * 5 * 5 # 管子的体积
        time = len(self.Pr_full) / 100
        # Kf = 0.02893 *Pr_last *Pr_last + 3.077 *Pr_last + 1572
        Kf = 12000 *(1+0.6*(Pr_last/600))
        Qin = self.get_Qin(time)
        Qout = self.get_Qout(time)

        next_Pr_d = (Kf)*(Qin-Qout)/v # 这 0.01ms 内压力的变化量
        self.Pr_full.append(Pr_last + next_Pr_d) # 把这 0.1ms 的压力放入结果

    def get_res(self):
        data = np.array(self.Pr_full)
        d = (data - np.ones(self.ranging)*100)*0.001
        sums = (d*d).sum()
        print(f'd{self.duration} sums{sums}')
        return sums

    def plot(self):
        x =  np.linspace(0,self.ranging/100,self.ranging)
        y = np.array(self.Pr_full)
        plt.plot(x,y,'r',label='original')
        # plt.scatter(x,y,c='g',label='')#散点图
        plt.show()


def main():
    x  = np.linspace(0.2,0.3,100)
    y = []
    
    
    min_res = 10
    last = Generator(0.1).get_res()
    for i in x:
        a = Generator(i)
        res = a.get_res()
        # print(f'res is {res} last is {last}')
        if res < last:
            last = res
        y.append(res)
    y = np.array(y)
    print(f'min is P{min_res}')
    plt.plot(x,y,'r',label='original')
    plt.scatter(x,y,c='g',label='before_fitting')#散点图
    plt.show()
    
if __name__ == '__main__':
    # main()
    # main()
    # 10s 
    # a = Generator(0.3244)
    a = Generator(0.3235)
    a.plot()