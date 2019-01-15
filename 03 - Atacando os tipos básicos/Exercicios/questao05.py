frase = "The Python Software Foundation and the global Python community welcome and encourage participation by everyone. Our community is based on mutual respect, tolerance, and encouragement, and we are working to help each other live up to these principles. We want our community to be more diverse: whoever you are, and whatever your background, we welcome you."

frase1 = frase.lower().split(" ", len(frase))
lista = []
lista2 = []
count = 0
for word in frase1:
    if word not in lista:
        lista.append(word)

for palavra in lista:
    if len(palavra) > 4:
        lista2.append(palavra)

for word in lista2:
    for letter in word:
        if letter in 'python':
            count+=1
            break
        
print('Frase: %s' %frase)
print('\n')
print('Palavras com mais de 4 caracteres: %s' %lista2)
print('\n')
print("Palavras que contenham 'python': %d" %count)
