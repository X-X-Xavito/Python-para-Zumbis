vetor = []
x = 0
soma = 0

while x < 4:
    n = float(input('Digite a nota: '))
    vetor.append(n)
    x += 1
    
x=0
while x < len(vetor):
    soma = soma + vetor[x]
    x+=1

y = 1
x = 0
while y < len(vetor) + 1:
    print('%d nota: %.1f' %(y,vetor[x]))
    y+=1
    x+=1

media = soma/len(vetor)

print('Media: %.2f' %media)

