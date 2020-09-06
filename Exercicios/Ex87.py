from random import randint
aposta = []
tot = []
cont = 0
total = 1
jogos = int(input('''Quantos jogos quer que eu sorteie?
'''))
while total <= jogos:
    cont = 0
    while True:
        numero = randint(1, 60)
        if numero not in aposta:
            aposta.append(numero)
            cont = cont + 1
        if cont >= 6:
            break
    tot.append(aposta[:])
    aposta.clear()
    total = total + 1
for j, l in enumerate(tot):
    print(f'Jogo {j}: {l}')





