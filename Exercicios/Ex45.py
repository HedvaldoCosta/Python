#45-Jokenpô
from  time import sleep
from random import randint
escolha = int(input('''Escolha:
[ 1 ] para PEDRA
[ 2 ] para TESOURA
[ 3 ] para PAPEL
Opcção:'''))
comp = randint (1,3)

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
if escolha == 1 and comp == 1:
    print('Você escolheu pedra')
    print('Computador escolheu pedra')
    print(' EMPATE')
elif escolha == 1 and comp == 2:
    print('Você escolheu pedra')
    print('Computador escolheu tesoura')
    print('VOCÊ VENCEU!')
elif escolha == 1 and comp == 3:
    print('Você escolheu pedra')
    print('Computador escolheu papel')
    print('VOCÊ PERDEU!')

elif escolha == 2 and comp == 1:
    print('Você escolheu tesoura')
    print('Computador escolheu pedra')
    print('VOCÊ PERDEU!')
elif escolha == 2 and comp == 2:
    print('Você escolheu tesoura')
    print('Computador escolheu tesoura')
    print('EMPATE')
elif escolha == 2 and comp == 3:
    print('Você escolheu tesoura')
    print('Computador escolheu papel')
    print('VOCÊ VENCEU!')

elif escolha == 3 and comp == 1:
    print('Você escolheu papel')
    print('Computador escolheu pedra')
    print('VOCÊ VENCEU!')
elif escolha == 3 and comp == 2:
    print('Você escolheu papel')
    print('Computador escolheu tesoura')
    print('VOCÊ PERDEU!')
elif escolha == 3 and comp == 3:
    print('Você escolheu papel')
    print('Computador escolheu papel')
    print('EMPATE')
