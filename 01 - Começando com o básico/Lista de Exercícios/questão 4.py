sal=int(input('Informe o seu salario atual: '))
aum=float(input('Informe a porcentagem do aumento salarial: '))
novo_sal= sal + (sal*(aum/100))
print('O novo salario é %.0f' %novo_sal)
