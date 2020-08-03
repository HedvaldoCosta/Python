# Faça um programa para ler diversos numeros inteiros e demonstrar o maior e o menor numero.
maior = menor = c = 0
while True:
    num = int(input('Me diga um numero[ 0 para sair ]: '))
    if num == 0:
        break
    c = c + 1
    if c == 1:
        maior = num
        menor = num
    else:
        if maior < num:
            maior = num
        if menor > num:
            menor = num
print(f'Maior numero: {maior}')
print(f'Menor numero: {menor}')