usuario = input('Usuario: ')
senha = input('Senha: ')

while usuario == senha:
    print('Usuario não pode ser igual a senha.')
    usuario = input('Usuario: ')
    senha = input('Senha: ')
    
print('Obrigado')
