#77-Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar,
# para cada palavra, quais são as suas vogais.

palavras = ('Aurora Boreal', 'Semana', 'Vegetal', 'Parceria', 'Funil', 'Kiwi')
for c in palavras:
    print(f'\nNa palavra \033[31m{c}\033[m temos: ', end='')
    for vogal in c:
        if vogal.lower() in 'aeiou':
            print(f'{vogal}', end=' ')
