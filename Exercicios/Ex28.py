#28-Advinhando um numero entre 0 e 5
from random import randint
from time import sleep
num = int(input('Diga-me um numero:'))
aleat = randint(0,5)
print('PROCESSANDO...')
sleep(1.5)
if aleat == num:
    print(f'Eu pensei no numero {aleat}. Você acertou!')
else:
    print('Errou')
    print(f'eu pensei no numero {aleat}')
