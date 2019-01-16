n = int(input('Digite um número: '))

x = 2
primos = []

#Descobrir a lista de números primos com o limite definido pelo usuario
while x < (n+1):
    y = 1
    count = 0
    while y < (n+1):
        if x % y == 0 and x != y:
            count+=1
        y+=1
    if count > 1:
        pass
    else:
        primos.append(x)
    x+=1
print('Lista de números primos: ')
print(primos)
print('A decomposição é: ')

#Calcular a decomposição usando a lista de números primos
quociente = n
z = 0
while quociente > 1:
    if quociente%primos[z] == 0:
        print('%d / %d' %(quociente, primos[z]))
        quociente = (quociente/primos[z])
    else:
        z+=1
print(1)


