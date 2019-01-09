'''
Pergunte a velocidade de um carro, supondo um valor inteiro.
Caso a velocidade esteja acima dos 110 km/h,
exiba uma mensagem dizendo que o usuario foi multado, e o valor da multa,
cobrando R$ 5,00 por km acima de 110.
'''

vel = int(input('Digite a velocidade do seu carro: '))
if vel <= 110:
    print('Você está dentro da velocidade permitida')
if vel > 110:
    vel = (vel - 110)*5
    print('Você foi multado! O valor da multa é R$ %5.2f' %vel)
