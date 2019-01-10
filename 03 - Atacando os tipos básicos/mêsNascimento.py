data = input('Data de nascimento(dd/mm/aaaa): ')

meses = ["janeiro", "feveiro", "março", "abril",
         "maio", "junho","julho","agosto","setembro",
         "outubro", "novembro", "dezembro"]

data = data.split('/')

data[1] = meses[int(data[1])-1]

data = ' de '.join(data)

print(data)
