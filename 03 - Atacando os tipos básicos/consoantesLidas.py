vetor = []
x=0

while x < 10:
    letra = input('Digite a primeira letra: ').lower()
    if letra not in 'aeiou':
        vetor.append(letra)
    x+=1
print('Foram lidas %d consoantes.' %len(vetor))
