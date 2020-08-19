#78-Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
lista = list()
for c in range(0, 5):
    lista.append(int(input(f'Me diga um numero na posição {c}: ')))
print(f'Numeros digitados: {lista}')
print(f'Maior numero: {max(lista)}')
print(f'Menor numero: {min(lista)}')
for n, v in enumerate(lista):
    if v == max(lista):
        print(f'Posição do maior: {n}')
    elif v == min(lista):
        print(f'Posição do menor: {n}')