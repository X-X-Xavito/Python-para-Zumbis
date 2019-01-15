conta = int(input('Valor da conta: '))
pagamento = int(input('Valor pago: '))

dif = pagamento - conta

print('Diferença: %d' %dif)

if dif > 0:
    if dif>=50:
        notas50 = dif/50
        resto50 = dif%50
        if resto50 == 0:
            print('Troco: %d nota(s) de 50' %(notas50))
        elif resto50 >=20:
            notas20 = resto50/20
            resto20 = resto50%20
            if resto20 == 0:
                print('Troco: %d nota(s) de 50 e %d nota(s) de 20' %(notas50, notas20))
            elif resto20 >= 10:
                notas10 = resto20/10
                resto10 = resto20%10
                if resto10 == 0:
                    print('Troco: %d nota(s) de 50 e %d nota(s) de 20 e %d nota(s) de 10' %(notas50, notas20,notas10))
                elif resto10 >= 5:
                    notas5 = resto10/5
                    resto5 = resto10%5
                    if resto5 == 0:
                        print('Troco: %d nota(s) de 50 e %d nota(s) de 20 e %d nota(s) de 10 e %d nota(s) de 5' %(notas50, notas20,notas10, notas5))
                    elif resto5>= 2:
                        notas2 = resto5/2
                        resto2 = resto5%2
                        if resto2 == 0:
                            print('Troco: %d nota(s) de 50 e %d nota(s) de 20 e %d nota(s) de 10 e %d nota(s) de 5 e %d nota(s) de 2' %(notas50, notas20,notas10, notas5, notas2))
                        elif resto2>= 1:
                            notas1 = resto2
                            resto1 = resto2%1
                            if resto1 == 0:
                                print('Troco: %d nota(s) de 50 e %d nota(s) de 20 e %d nota(s) de 10 e %d nota(s) de 5 e %d nota(s) de 2 e %d nota(s) de 1' %(notas50, notas20,notas10, notas5, notas2, notas1))

        elif resto50>=10:
            notas10 = resto50/10
            resto10 = resto50%10
            if resto10 == 0:
                    print('Troco: %d nota(s) de 50 e %d nota(s) de 10' %(notas50, notas10))
            elif resto10 >= 5:
                    notas5 = resto10/5
                    resto5 = resto10%5
                    if resto5 == 0:
                        print('Troco: %d nota(s) de 50  e %d nota(s) de 10 e %d nota(s) de 5' %(notas50,notas10, notas5))
                    elif resto5>= 2:
                        notas2 = resto5/2
                        resto2 = resto5%2
                        if resto2 == 0:
                            print('Troco: %d nota(s) de 50 e %d nota(s) de 10 e %d nota(s) de 5 e %d nota(s) de 2' %(notas50, notas10, notas5, notas2))
                        elif resto2>= 1:
                            notas1 = resto2
                            resto1 = resto2%1
                            if resto1 == 0:
                                print('Troco: %d nota(s) de 50 e %d nota(s) de 10 e %d nota(s) de 5 e %d nota(s) de 2 e %d nota(s) de 1' %(notas50, notas10, notas5, notas2, notas1))

        elif resto50>=5:
            notas5 = resto50/5
            resto5 = resto50%5
            if resto5 == 0:
                print('Troco: %d nota(s) de 50 e %d nota(s) de 5' %(notas50, notas5))
        elif resto50>=2:
            notas2 = resto50/2
            resto2 = resto50%2
            if resto2 == 0:
                print('Troco: %d nota(s) de 50 e %d nota(s) de 2' %(notas50, notas2))
        elif resto50>=1:
            notas1 = resto50
            resto1 = resto50%1
            if resto1 == 0:
                print('Troco: %d nota(s) de 50 e %d nota(s) de 1' %(notas50, notas1))
               

    '''
    elif dif>=20:
    elif dif>=10:
    elif dif>= 5:
    elif dif>= 2:
    elif dif>= 1:
    '''
else:
    print('Não é necessario troco.')






"""
if dif > 0:
    if dif >= 50:
        notas50 = dif/50
        resto50 = dif%50
        if resto50 == 0:
            print('Troco: %d nota(s) de 50' %(notas50))
        else:
            if resto50 >= 20:
                notas20 = resto50/20
                if (resto50)%20 == 0:
                    print('Troco: %d nota(s) de 50 e %d nota(s) de 20' %(notas50, notas20))
                else:
            else:
                if resto50>=10:
                   ''' xxxx'''
                else:
                    if resto50 >=5:
                        ''' xxxx'''
                    else:
                        if resto50 >= 2:
                            ''' xxxx'''
                        else:
                            if resto50 >= 2:
                                ''' xxxx'''
                            else:
                                if resto50 >= 1:
                                    ''' xxxx'''
    else:
"""

'''
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
             
'''
