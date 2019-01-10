n = int(input('N: '))
a,b = 1,1
x = 1

while x <= n-2:
    a,b = b, a+b
    x = x +1
print('Fib(%d): %d'%(n, b))
