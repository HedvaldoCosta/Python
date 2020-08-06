# João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.
# Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca
# do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente.
# João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso.
# Gravar na variável excesso a quantidade de quilos além do limite
# e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.

peixes = int(input('Numero de peixes pegos hoje: '))
smulta = sexc = 0
for c in range(1, peixes + 1):
    peso = float(input(f'\nPeso do {c}º peixe: '))
    if peso > 50:
        excesso = peso - 50
        multa = excesso * 4
        smulta = smulta + multa
        sexc = sexc + excesso
        print(f'{peso:.<10}', end=' ')
        print(f'Excesso: {excesso:>3}KG', end='   ')
        print(f'multa: {multa}R$', end=' ')
    else:
        print('Peixe com o peso adequado')
print(f'\nQuantidade de excesso total: {sexc}KG')
print(f'\nMulta total: {smulta}R$')
