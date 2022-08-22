import numpy as np
res = {}
x = []; y = []
with open('PaP.txt','r') as f:
    raw = f.readlines()
    for i in range(len(raw)):
        [key , value] = raw[i].replace('\n','').split('\t')
        x.append(float(key))
        y.append(float(value))

def __sst(y_no_fitting):
    """
    计算SST(total sum of squares) 总平方和
    :param y_no_predicted: List[int] or array[int] 待拟合的y
    :return: 总平方和SST
    """
    y_mean = sum(y_no_fitting) / len(y_no_fitting)
    s_list =[(y - y_mean)**2 for y in y_no_fitting]
    sst = sum(s_list)
    return sst


def __ssr(y_fitting, y_no_fitting):
    """
    计算SSR(regression sum of squares) 回归平方和
    :param y_fitting: List[int] or array[int]  拟合好的y值
    :param y_no_fitting: List[int] or array[int] 待拟合y值
    :return: 回归平方和SSR
    """
    y_mean = sum(y_no_fitting) / len(y_no_fitting)
    s_list =[(y - y_mean)**2 for y in y_fitting]
    ssr = sum(s_list)
    return ssr


def __sse(y_fitting, y_no_fitting):
    """
    计算SSE(error sum of squares) 残差平方和
    :param y_fitting: List[int] or array[int] 拟合好的y值
    :param y_no_fitting: List[int] or array[int] 待拟合y值
    :return: 残差平方和SSE
    """
    s_list = [(y_fitting[i] - y_no_fitting[i])**2 for i in range(len(y_fitting))]
    sse = sum(s_list)
    return sse


def goodness_of_fit(y_fitting, y_no_fitting):
    """
    计算拟合优度R^2
    :param y_fitting: List[int] or array[int] 拟合好的y值
    :param y_no_fitting: List[int] or array[int] 待拟合y值
    :return: 拟合优度R^2
    """
    SSR = __ssr(y_fitting, y_no_fitting)
    SST = __sst(y_no_fitting)
    rr = SSR /SST
    return rr

print(x,y)

from matplotlib import pyplot as plt
 
# def f(x):
#     return x**2+1
x=np.array(x)
y=np.array(y)
def f_fit(x,y_fit):
    a,b,c=y_fit.tolist()
    return a*x**2+b*x+c
# x=np.linspace(-5,5)
# y=f(x)+np.random.randn(len(x))#加入噪音
y_fit=np.polyfit(x,y,2)#二次多项式拟合
y_show=np.poly1d(y_fit)#函数优美的形式


print(y_show)#打印
y1=f_fit(x,y_fit)
plt.plot(x,y,'r',label='original')
plt.scatter(x,y,c='g',label='before_fitting')#散点图
plt.plot(x,y1,'b--',label='fitting')
plt.title('polyfitting')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()#显示标签
plt.show()

f = lambda x : 0.02893 * x * x + 3.077 * x + 1572

print(goodness_of_fit(f(x),y))