n = input('Palavra: ').lower()
palavra = ''
x = 0

while len(n) != len(palavra):
    if n[x] not in 'aeiou':
        palavra = palavra + n[x]
    else:
        palavra = palavra + '*'
    x+=1

print(palavra)
