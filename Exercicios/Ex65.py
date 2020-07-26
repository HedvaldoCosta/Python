# Maior e menor
soma = c = maior = menor = 0
resp = 'S'
while resp == 'S':
    num = int(input('Numero: '))
    c= c + 1
    soma = soma + num
    if c == 1:
        maior = num
        menor = num
    elif num > maior:
        maior = num
    elif num < menor:
        menor = num
    resp = str(input('Quer continuar? [S/N]')).upper().strip()[0]
print(f'Você digitou {c} números e a Média entre eles é: {soma/c:.2f}')
print(f'Maior numero: {maior}')
print(f'Menor numero: {menor}')

