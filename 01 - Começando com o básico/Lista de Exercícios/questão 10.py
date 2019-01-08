cigar_dia = int(input('Quantos cigarros você fuma por dia? '))
anos_fumo = int(input('Anos fumando: '))

'''
A cada cigarro: menos 10 minutos de vida.
Um dia tem: 1440 minutos
Um ano tem 525600 minutos
'''

cigar_dias = cigar_dia*(10/1440)
anos_fumo = (cigar_dias * anos_fumo* 365)
total = anos_fumo

print('Você perdeu aproximadamente %.2f dias' %total)
