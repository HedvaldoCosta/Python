# Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores
# Aceitando apenas valores entre 0 e 1000
c = menor = maior = soma = 0
while True:
    c = c + 1
    num = int(input('''Diga-me um numero [Não aceitando numeros menores que 0 ou maiores que 1000]: '''))
    if num < 0 or num > 1000:
        break
    soma = soma + num
    if c == 1:
        maior = num
        menor = num
    else:
        if maior < num:
            maior = num
        elif num < menor:
            menor = num
print(f'Menor numero: {menor}')
print(f'Maior numero: {maior}')
print(f'Soma: {soma}')

