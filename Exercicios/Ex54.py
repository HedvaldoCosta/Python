# Maior idade
from datetime import date
sm = 0
ss = 0
atual = date.today().year
for c in range(1, 8):
    ano = int(input(f'ano de nascimento da {c}º pessoa : '))
    idade = atual - ano
    if idade >= 18:
        ss = ss + 1
    else:
        sm = sm + 1
print(f"Numero de pessoas com maior idade:{ss}")
print(f"Numero de pessoas com menor idade: {sm}")