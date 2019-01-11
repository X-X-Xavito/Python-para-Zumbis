frase = "The Python Software Foundation and the global Python community welcome and encourage participation by everyone. Our community is based on  mutual respect, tolerance, and encouragement, and we are working to help each other live up to these principles. We want our community to be more diverse: whoever you are, and whatever your background, we welcome you."

frase = frase.lower()
novo_vetor = []

vetor = frase.split()

x = 0

print(vetor[0][-1])

while x < len(vetor)-1:
    if vetor[x][0] or vetor[x][-1] in 'python':
        novo_vetor.append(vetor[x])
    x+=1
print(novo_vetor)
