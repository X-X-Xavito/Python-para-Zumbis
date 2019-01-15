n = int(input('N: '))
k = 1
a,b,c = 1,2,3
triangular = False

while k<=n:
    if a*b*c == n:
        triangular = True
    else:
        a = b
        b = b+1
        c = c+1
    k = k+1

if triangular == True:
    print('Triangular: %d * %d * %d: %d' %(a,b,c,n))
else:
    print('Não triangular')
