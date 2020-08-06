# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que
# a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário
# a quantidades de latas de tinta a serem compradas e o preço total.
from math import ceil
tam = float(input('Tamanho da area a ser pintada: '))
tinta = (tam / 3) / 18
print(f'Latas de tinta: {ceil(tinta)}')
print(f'Valor a ser pago: {ceil(tinta) * 80}')