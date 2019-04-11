import numpy as np
import matplotlib
import matplotlib.pyplot as plt

par=input('Введите параметр распределения Парето (например, 0.1): ')
par=float(par)
quant=input('Введите общее количество точек в распределении Парето (например, 100000): ')
quant=int(quant)
def histogram(ax, data, bins, cumulative=False, x_label = "", y_label = "", title = ""):
    ax.hist(data, bins = bins, cumulative = cumulative)
    ax.set_ylabel(y_label)
    ax.set_xlabel(x_label)
    ax.set_title(title)
s = np.random.pareto(par,quant)
fig, ax = plt.subplots(1,1)
fig.set_size_inches (7,4)
m=np.mean([i for i in s if i <=200])
histogram(ax,s,np.linspace(0,m,100))