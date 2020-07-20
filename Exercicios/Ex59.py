# Menu
numero1 = float(input('Diga-me um numero: '))
numero2 = float(input('Outro: '))
escolha = 0
while escolha != 5:
    escolha = int(input('''[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novo numero
[ 5 ] sair
sua escolha: '''))
    if escolha == 1:
        print(f'{numero2} + {numero1} = {numero2 + numero1}')
    elif escolha == 2:
        print(f'{numero2} * {numero1} = {numero1 * numero2}')
    elif escolha == 3:
        if numero1 > numero2:
            print(f'{numero1} > {numero2}')
        elif numero1 == numero2:
            print('Numero iguais')
        else:
            print(f'{numero2} > {numero1}')

    elif escolha == 4:
        numero1 = float(input('Diga-me um numero: '))
        numero2 = float(input('Outro: '))
    elif escolha == 5:
        print('\033[31m FIM DO PROGRAMA')
    else:
        print('OPÇÃO INVALIDA')