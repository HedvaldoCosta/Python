# Faça um programa que leia 5 números e informe a soma e a média dos números.
soma = 0
for c in range(1, 6):
    num = int(input(f'{c}º Numero: '))
    soma = soma + num
print(f'A soma entre esses numeros é igual a {soma} e a média entre eles é de {soma/c:.2f} ')
