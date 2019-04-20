num=input('Введите максимальное число, ограничивающее массив простых чисел...')
    
def is_pr(x):
    m=1
    for i in range(2,int(x/2)+1):
        m=(x%i!=0)
        if m==False:
            break
    return m

def nums(n = 1):
    while(True):
        if is_pr(n): 
            yield n
        n += 1
for n in nums():
    if n > int(num): 
        break
    print(n)

