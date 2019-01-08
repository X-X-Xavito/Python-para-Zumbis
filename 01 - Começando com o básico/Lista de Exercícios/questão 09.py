km_perc = int(input('Quantos km foram percorridos? '))
dias = int(input('Por quantos dias o carro foi alugado?'))

valor_km = km_perc*0.15
valor_dias = dias * 60

valor_final = valor_km + valor_dias

print('O valor a ser pago é R$ %.2f'%valor_final)
