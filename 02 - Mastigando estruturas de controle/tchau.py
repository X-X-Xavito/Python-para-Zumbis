'''
A empresa Tchau de telefonia cobra:
-Abaixo de 200 minutos, R$ 0,20 por minuto
-Entre 200 e 400 minutos, R$ 0,18 por minuto
-Acima de 400 minutos, R$ 0,15 por minuto


- Bonus: - Acima de 800 minutos, R$ 0,08
Calcule a conta de telefone
'''

minutos = int(input('Minutos utilizados: '))

if minutos > 800:
    total = minutos * 0.08
elif minutos > 400 and minutos <= 800:
    total = minutos * 0.15
elif minutos < 200:
    total = minutos * 0.2
else:
    total = minutos * 0.18

print('Valor da conta: R$ %.2f' %total)
