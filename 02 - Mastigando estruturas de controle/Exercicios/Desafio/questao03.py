n = int(input('N: '))

count = 0

if n == 1 or n ==2:
    print('É primo')
else:
    for numero in range(2,n):
        if n%numero == 0:
            count+=1
    if count != 0:
        print('Não é primo')
    else:
        print('É primo')
