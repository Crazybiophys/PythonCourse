from numpy import linspace
x1,x2,N=input('Шаг 2. Введите начало и конец интегрирования и количество точек в интервале через пробел...\n').split(' ')
x1=float(x1)
x2=float(x2)
N=float(N)
x=linspace(x1,x2,N)
f=5+0*x #Шаг 1. Задайте функцию в коде 
dx=(x2-x1)/(N-1)
I=0
for i in range(len(x)-1):
    I+=((f[i]+f[i-1])/2)*dx
print ('Шаг 3. Интеграл Вашей функции: ',I)