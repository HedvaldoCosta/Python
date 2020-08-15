#55-Maior e menor peso
menor = 0
maior = 0
for c in range(1, 6):
    peso = float(input(f'Peso da {c}º pessoa: '))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print(f'Maior peso:{maior}KG')
print(f'Menor peso:{menor}KG')
