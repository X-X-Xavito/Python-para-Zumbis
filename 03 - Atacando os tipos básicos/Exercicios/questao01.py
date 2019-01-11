import random
'''
lista = []
maior = 0
menor = 100 
while len(lista) < 10:
    n = random.randint(1,100)
    if n not in lista:
        lista.append(n)
    if (100 - n) < (100-maior):
        maior = n
    if (100-n)  > (100-menor):
        menor = n
lista.sort()

print('Lista: %s' %lista)
print('Maior: %d' %maior)
print('Menor: %d '%menor)
'''

lista = []

while len(lista)<10:
    n = random.randint(1,100)
    if n not in lista:
        lista.append(n)

lista.sort()
print(lista)
print('Menor: %d' %lista[0])
print('Maior: %d' %lista[len(lista)-1])
