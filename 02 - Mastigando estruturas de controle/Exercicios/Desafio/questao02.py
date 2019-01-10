conta = int(input('Valor da conta: '))
pagamento = int(input('Valor pago: '))

if pagamento > conta:
    dif = pagamento - conta
    if dif%50 == 0:
        troco = dif/50
        print('Troco: %d nota(s) de 50' %troco)
    else:
        if dif%20 == 0:
            troco = dif/20
            print('Troco: %d nota(s) de 20' %troco)
        else:
            if dif%10 == 0:
                troco = dif/10
                print('Troco: %d nota(s) de 10' %troco)
            else:
                if dif%5 == 0:
                    troco = dif/5
                    print('Troco: %d nota(s) de 5' %troco)
                else:
                    if dif%2 == 0:
                        troco = dif/2
                        print('Troco: %d nota(s) de 2' %troco)
                    else:
                        if dif%1 == 0:
                            troco = dif/1
                            print('Troco: %d nota(s) de 1' %troco)
             
