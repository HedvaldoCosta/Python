# Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares
# e a quantidade de números impares.
numI = numP = 0
for c in range(1, 11):
    num = int(input('Me diga um numero: '))
    if num % 2 == 0:
        numP = numP + 1
    else:
        numI = numI + 1
print(f'Numero de pares: {numP}')
print(f'Numero de impares: {numI}')
