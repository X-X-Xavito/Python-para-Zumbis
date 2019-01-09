ano = int(input('Digite o ano: '))

if ano%4 == 0:
    if ano%100 != 0:
        print('Ano Bisexto')
    else:
        print('Ano não bisexto')
else:
    if ano%400 == 0:
        print('Ano bisexto')
    else:
        print('Ano não Bisexto')
    
        
