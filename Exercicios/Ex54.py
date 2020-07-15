# Maior idade
sm = 0
ss = 0
for c in range(1, 8):
    idade = int(input(f'Idade da {c}º pessoa : '))
    if idade < 18:
        ss = ss + 1
    else:
        sm = sm + 1
print(f"Numero de pessoas com menor idade:{ss}")
print(f"Numero de pessoas com maior idade: {sm}")