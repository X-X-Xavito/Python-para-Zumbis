val_hora = float(input('Valor das horas: R$ '))
horas_tra = float(input('Horas trabalhadas no mês: '))

sal_Bruto = val_hora * horas_tra
ir = sal_Bruto*0.11
inss = sal_Bruto*0.08
sind = sal_Bruto*0.05

sal_liq = sal_Bruto - ir - inss - sind


print('Salário Bruto: R$ %.2f' %sal_Bruto)
print('- IR: R$ %.2f' %ir)
print('- INSS: R$ %.2f' %inss)
print('- Sindicato: R$ %.2f' %sind)
print('Salario Líquido: R$ %.2f' %sal_liq)

