notas = [1,2,3,4,5]
cont = 0
soma = 0

while cont < len(notas):
    soma += notas[cont]
    cont += 1

resultado = soma/len(notas)
print(resultado)
