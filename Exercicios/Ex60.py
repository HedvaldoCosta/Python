# fatorial
num = int(input('Diga-me um numero: '))
cont = num
mult = 1
print(f'{num}! = ', end=' ')
while cont > 0:
    print(f'{cont}', end= ' ')
    print(' X 'if cont > 1 else ' = ', end=' ')
    mult = mult * cont
    cont = cont - 1
print(mult)



