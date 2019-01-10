a = int(input('Dividendo: '))
b = int(input('Divisor: '))
resto = a%b

while resto != 0:
    a = b
    b = resto
    resto = a%b
print('mdc: %d' %b)

        
