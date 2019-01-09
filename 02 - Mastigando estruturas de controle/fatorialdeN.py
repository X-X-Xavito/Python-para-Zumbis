n = 1
produto = 1
x = int(input('Digite um numero: '))

while n <= x:
    produto = produto*n
    n = n+1

print('Fatorial de %d: %d'%(x,produto))

