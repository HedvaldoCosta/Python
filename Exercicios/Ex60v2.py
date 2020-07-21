# Usando for
f = 1
n = int(input('Me diga um numero: '))
print(f'{n}! = ', end=' ')
for c in range(n, 0, -1):
    f = f * c
    print(f'{c}', end=' ')
    print('X' if c > 1 else ' = ', end=' ')
print(f)
