
frase = "The Python Software Foundation and the global Python community welcome and encourage participation by everyone. Our community is based on mutual respect, tolerance, and encouragement, and we are working to help each other live up to these principles. We want our community to be more diverse: whoever you are, and whatever your background, we welcome you."


frase1 = frase.lower().split(" ", len(frase))
lista = []
for word in frase1:
    if word[0] in 'python':
        lista.append(word)
    elif word[-1] in 'python':
        lista.append(word)

print('Frase: %s' %frase)
print('\n')
print('Lista de Palavras: %s' %lista)
