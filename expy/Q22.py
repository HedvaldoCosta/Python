# Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores.
# Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato
from random import randint
vtA = vtB = vtC = 0
eleit = int(input('Numero de eleitores: '))
esc = int(input('''Deseja que a maquina vote para você?
[ 1 ] SIM
[ 2 ] NÃO
Sua opção: '''))
if esc == 1:
    for c in range(1, eleit + 1):
        rand = randint(1, 3)
        if rand == 1:
            vtA = vtA + 1
        elif rand == 2:
            vtB = vtB + 1
        elif rand == 3:
            vtC = vtC + 1
if esc == 2:
    for c in range(1, eleit + 1):
        voto = int(input('''[ 1 ] para o candidato A
[ 2 ] para o candidato B
[ 3 ] para o candidato C
[ 4 ] para sair
Sua opção: '''))
        if voto == 1:
            vtA = vtA + 1
        elif voto == 2:
            vtB = vtB + 1
        elif voto == 3:
            vtC = vtC + 1
        else:
            break
print(f'Numero de votos para o candidato A: {vtA}')
print(f'Numero de votos para  o candidato B: {vtB}')
print(f'Numero de votos para o candidato C: {vtC}')
if (vtA > vtC) and (vtA > vtB):
    print('Candidato A ganhou')
elif (vtB > vtA) and (vtB > vtC):
    print('Candidato B ganhou')
elif (vtC > vtB) and (vtC > vtA):
    print('Candidato C ganhou')
else:
    print('Empate')