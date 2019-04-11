import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

max_poisson=input('Введите максимум распределения Пуассона (например, 5): ')
max_poisson=float(max_poisson)
quant=input('Введите общее количество точек в распределении Пуассона (например, 10000): ')
quant=int(quant)
def histogram(ax, data, bins, cumulative=False, x_label = "", y_label = "", title = ""):
    ax.hist(data, bins = bins, cumulative = cumulative,rwidth=0.2)
    ax.set_ylabel(y_label)
    ax.set_xlabel(x_label)
    ax.set_title(title)
s = np.random.poisson(max_poisson,quant)
fig, ax = plt.subplots(1,1)
fig.set_size_inches (9,3)
smin=s[np.argmin(s)]
smax=s[np.argmax(s)]
histogram(ax,s,np.linspace(smin-0.5,smax+0.5,smax-smin+2),x_label = "Целое число", y_label = "Количество попаданий", title = "Распределение Пуассона")