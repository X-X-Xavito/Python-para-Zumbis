"""import random

lista= []
while len(lista) < 15:
    n = random.randint(10,100)
    if n not in lista:
        lista.append(n)

lista.sort()
print(len(lista))
print(lista)
"""
import random

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
print(len(lista))
print(lista)
print(maior)
print(menor)
