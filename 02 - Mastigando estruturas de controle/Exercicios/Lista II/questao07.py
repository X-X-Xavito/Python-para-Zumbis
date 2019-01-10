tamanho = float(input('Digite o tamanho em m²: '))

if tamanho <= 54:
    latas = 1
    preço = 80
    print('Latas: %d \nPreço: R$ %.2f' %(latas, preço))
else:
    if tamanho%54 == 0:
        latas = (tamanho/54)
        preço = latas * 80
        print('Latas: %d \nPreço: R$ %.2f' %(latas, preço))
    else:
        latas = int((tamanho/54)) + 1
        preço = latas * 80
        print('Latas: %d \nPreço: R$ %.2f' %(latas, preço))
