n = int(input('N: '))

x = 2
primo = True
count = 0

for numero in range(2,n):
    if n%numero == 0:
        count+=1

if count != 0:
    print('Não é primo')
else:
    print('É primo')
