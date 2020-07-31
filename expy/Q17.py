# Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120
num = int(input('Numero para o fatorial: '))
fat = 1
print(f'{num}! = ', end='')
for c in range(num, 0, -1):
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    fat = fat * c
print(f' {fat}')