# -*- coding: utf-8 -*-
number=input('Введите положительное целое число и нажмите ENTER... ')
if number.isdigit()==True:
    sum=0
    pro=1
    for digit in number:
        sum+=int(digit)
        pro*=int(digit)
    print ('Сумма цифр введенного числа: ',sum ,'Произведение этих цифр: ',pro)