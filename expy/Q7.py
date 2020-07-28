# Faça um programa que leia 5 números e informe o maior número.
maior = 0
for c in range(1, 6):
    num = int(input(f'{c}º Numero: '))
    if c == 1:
        maior = num
    else:
        if num > maior:
            maior = num
print(f'Maior numero: {maior}')