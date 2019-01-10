n = int(input('N: '))
k = 1
a,b,c = 1,2,3

while k<=n:
    if a*b*c == n:
        print('Triangular: %d * %d * %d: %d' %(a,b,c,n))
    else:
        a = b
        b = b+1
        c = c+1
    k = k+1
