peso = float(input('Digite o peso de peixes: '))
excesso = 0
multa = 0

if peso > 50:
    excesso = peso - 50
    multa = excesso * 4
    print('Peso: %.2f\nExcesso: %.2f\nMulta: R$ %.2f' %(peso,excesso,multa))
else:
    print('Peso: %.2f\nExcesso: %.2f\nMulta: R$ %.2f' %(peso, excesso, multa))
