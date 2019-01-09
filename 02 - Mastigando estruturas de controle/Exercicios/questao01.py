a = int(input('Valor do primeiro lado: '))
b = int(input('Valor do segundo lado: '))
c = int(input('Valor do terceiro lado: '))

somaAB = a+b
somaAC = a+c
somaBC = b+c

if somaAB > c and somaAC > b and somaBC > a:
    if a == b and a == c:
        print('triangulo equilatero')
    elif a == b and a != c:
        print('triangulo isósceles')
    else:
        print('triangulo escaleno')
else:
    print('Não é possivel formar um triangulo')
