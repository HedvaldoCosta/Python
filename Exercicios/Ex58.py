#Jogo da adivinhação
from random import randint
c = 0
aleat = randint(1, 10)
numero = 11
while aleat != numero:
    numero = int(input('Adivinhe que número estou pensando: '))
    c = c + 1
    if numero == aleat:
        print(f'Você acertou! Eu pensei no numero {aleat}')
    else:
        if numero < aleat:
            print('Numero abaixo do que eu pensei...')
        if numero > aleat:
            print('Numero acima do que eu pensei...')


print(f'Numero de tentativas:{c}')
