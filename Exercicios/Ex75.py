# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
#
# A) Quantas vezes apareceu o valor 9.
#
# B) Em que posição foi digitado o primeiro valor 3.
#
# C) Quais foram os números pares.

num = (int(input('Me diga um numero: ')), int(input('Me diga um numero: ')), int(input('Me diga um numero: ')),
       int(input('Me diga um numero: ')))
print(f'Vezes que o 9 apareceu: {num.count(9)}')
if 3 in num:
    print(f'O numero 3 apareceu na posição {num.index(3)+1}')
else:
    print('Valor 3 não encontrado')
print('Numeros pares:')
for n in num:
    if n % 2 == 0:
        print(f'{n} ', end=' ')



