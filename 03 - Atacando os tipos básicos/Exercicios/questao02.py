import random

lista = []
par = []
impar = []

while len(lista) < 10:
    n = random.randint(1,100)
    if n not in lista:
        lista.append(n)
        if n%2 ==0:
            par.append(n)
        else:
            impar.append(n)
lista.sort()
par.sort()
impar.sort()
print('Lista: %s' %lista)
print('Pares: %s' %par)
print('Impares: %s' %impar)
