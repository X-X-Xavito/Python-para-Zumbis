a = int(input('Primeiro número: '))
b = int(input('Segundo número: '))
c = int(input('Terceiro número: '))

if a > b and a > c:
    print('Maior número: %d' %a)
elif b > a and b > c:
    print('Maior número: %d' %b)
elif c > a and c > b:
    print('Maior número: %d' %c)
