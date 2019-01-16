conta = int(input('Valor da conta: '))
pagamento = int(input('Valor pago: '))

dif = pagamento - conta

print('Diferença: %d' %dif)

notas = [50,20,10,5,2,1]

for n in notas:
    if dif < n:
        pass
    else:
        count = dif/n
        dif = dif%n
        print('%d nota(s) de %d' %(count,n))
        
