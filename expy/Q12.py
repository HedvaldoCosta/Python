# Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10.
# O usuário deve informar de qual numero ele deseja ver a tabuada.
while True:
    num = int(input('''Deseja ver a tabuada de qual numero? [ 999 para sair ]
R: '''))
    if num == 999:
        break
    for c in range(1, 11):
        print(f'{num} X {c} = {num * c}')
