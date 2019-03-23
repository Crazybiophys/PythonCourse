enter_data=input('Введите желаемый список целых чисел через пробел:')
list_of_numbers=enter_data.split(' ')

all=[]
for symbol in list_of_numbers:
    if symbol.isdigit()==True:
        all.append(int(symbol))
    else:
        print('Это не целое число: ',symbol)
print('Ваш список чисел: ',all)

for num in range(len(all)):
    big=[]
    for symbol in all[num:]:
        if symbol>all[num]:
            big.append(symbol)
            continue
        else:
            continue
    if big!=[]:
        print('Число из списка: ',all[num],'; Последующие числа, больше его: ', big)
    else:
        continue
