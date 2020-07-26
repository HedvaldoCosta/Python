# Par ou impar
from random import randint
s = c = 0
while True:
    valor = int(input('Me diga um valor: '))
    rand = randint(0, 10)
    opc = ' '
    while opc not in 'PI':
        opc = str(input('[\033[36mP\033[m] para par e [\033[31mI\033[m] para impar: ')).upper().strip()[0]
    if opc == 'P':
        s = rand + valor
        if s % 2 == 0:
            print(f'Você jogou {valor} e a maquina {rand} dando {s}. \033[32mGANHOU!\033[m')
        else:
            print(f'Você jogou {valor} e a maquina {rand} dando {s}. \033[31mPERDEU!\033[m')
            break
    if opc == 'I':
        s = rand + valor
        if s % 2 == 0:
            print(f'Você jogou {valor} e a maquina {rand} dando {s}. \033[31mPERDEU!\033[m')
            break
        else:
            print(f'Você jogou {valor} e a maquina {rand} dando {s}. \033[32mGANHOU!\033[m')
    c = c + 1
print(f'Numero total de vitorias seguidas: {c}')
