#  Crie um programa que gere cinco números aleatórios e os coloque em uma tupla.
#  Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
from random import randint
rand = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), )
print(f'Numeros sorteados: {rand}')
print(f'Maior valor sorteado: {max(rand)}')
print(f'Menor valor sorteado: {min(rand)}')
