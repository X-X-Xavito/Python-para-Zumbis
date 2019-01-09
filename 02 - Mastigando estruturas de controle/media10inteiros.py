n = 1
soma = 0

while n <= 10:
    x = int(input('Digite o %d numero: ' %n))
    soma = soma + x
    n = n+1
media = soma/10
print('Media: %5.2f'%media)
