# Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número
# elevado ao segundo número. Não utilize a função de potência da linguagem.
pot = 1
base = int(input('Base: '))
exp = int(input('Expoente: ')) + 1
for c in range(1, exp):
    pot = base * pot
print(f'Potencia = {pot}')



