dias = int(input('Digite a quantidade de dias: '))
horas = int(input('Digite a quantidade de horas: '))
minutos = int(input('Digite os minutos: '))
segundos = int(input('Digite os segundos: '))

minutos = minutos * 60
horas = horas * 60 * 60
dias = dias * 24 * 60 * 60

total = minutos + horas + dias + segundos

print('%d segundos' %total)
