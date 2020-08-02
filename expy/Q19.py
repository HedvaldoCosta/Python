# Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.
# Um número primo é aquele que é divisível somente por ele mesmo e por 1.
cont = 0
num = int(input('Numero: '))
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[31m', end='')
        cont = cont + 1
    else:
        print('\033[m', end='')
    print(f' {c} ', end='')
if cont == 2:
    print('''
Numero primo''')
else:
    print('''
Numero não primo''')

