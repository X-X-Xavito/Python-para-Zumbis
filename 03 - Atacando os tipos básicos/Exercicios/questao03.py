import random

lista1=[]
lista2=[]
final=[]

while len(lista1) < 10:
    n = random.randint(1,100)
    if n not in lista1:
        lista1.append(n)
lista1.sort()

print(lista1[0])

while len(lista2) < 10:
    n = random.randint(1,100)
    if n not in lista2:
        lista2.append(n)
lista2.sort()


x = 0
y = 0
while len(final) < 20:
    if x == 0 or x%2 == 0:
        final.append(lista1[x])
    else:
        final.append(lista2[y])
        y+=1
    x+=1
    
"""
x = 0
while len(final) < 20:
    if len(final) == 0 or len(final)%2 ==0:
        final.append(lista1[x])
    else:
        final.append(lista2[x])
    x+=1
"""


print(lista1)
print(lista2)
