with open('C://rosalind_fib.txt') as text:
    n,k=text.read().split(' ')
    n=int(n)
    k=int(k)
fib=[1,1]

def fibonacci(n,k):
    for month in range(n-2):
        fib.append(fib[month]*k+fib[month+1])
    return fib, fib[-1]

print (fibonacci(n,k))
    