#60-fatorial
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

OU

f = 1
n = int(input('Me diga um numero: '))
print(f'{n}! = ', end=' ')
for c in range(n, 0, -1):
    f = f * c
    print(f'{c}', end=' ')
    print('X' if c > 1 else ' = ', end=' ')
print(f)


