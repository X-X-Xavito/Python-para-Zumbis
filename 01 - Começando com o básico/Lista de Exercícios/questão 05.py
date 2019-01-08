preco = int(input('Digite o preço do produto: '))
taxa = int(input('Digite o percentual do desconto: '))

desconto = preco * (taxa/100)
novo_preço = preco - desconto

print('O valor do desconto é: ' + str(desconto))
print('O novo preço do produto é: ' + str(novo_preço))


