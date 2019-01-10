n = input('Palavra: ').lower()

if n == n[::-1]:
    print('%s é palíndrome'  %n)
else:
    print('%s não é palíndrome' %n)
