from random import randint
def sorteia(numeros):
    for contador in range(1, 6):
        n = randint(1, 10)
        numeros.append(n)
        print(f'{n}', end=' ')


def somapares(numeros):
    soma = 0
    for c in numeros:
        if c % 2 == 0:
            soma += c
    print(f'\n A soma dos valores é igual a {soma}')


numero = []
sorteia(numero)
somapares(numero)
