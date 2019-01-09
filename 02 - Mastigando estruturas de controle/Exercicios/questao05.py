a = int(input('Primeiro número: '))
b = int(input('Segundo número: '))
c = int(input('Terceiro número: '))

if a > b and a > c:
    print('Maior número: %d' %a)
    if b > c:        
        print('Menor número: %d' %c)
    else:
        print('Menor número: %d' %b)
elif b > a and b > c:
    print('Maior número: %d' %b)
    if a > c:
        print('Menor número: %d' %c)
    else:
        print('Menor número: %d' %a)
elif c > a and c > b:
    print('Maior número: %d' %c)
    if a > b:
        print('Menor número: %d' %b)
    else:
        print('Menor número: %d' %a)
