from time import sleep
from datetime import date
numero = [0, 1]
senha = 121210


# pegar caixa
def pegar_caixa():
    sleep(0.6)
    print('Avançando o braço...')
    sleep(0.6)
    print('Abaixando o braço...')


#função caminhão
def caminhao():
    carga_caminhao = str(input('''O caminhão está esperando carga? [S/N]
''')).strip().upper()
    while carga_caminhao == 'N':
        sleep(1)
        carga_caminhao = str(input('''O caminhão está esperando carga? [S/N]
''')).strip().upper()
    if carga_caminhao == 'S':
        carga_terminal = int(input('''Quantas caixas para entregar?
'''))
        for contador in range(1, carga_terminal+1):
            pegar_caixa()
    while carga_caminhao not in 'SN':
        carga_caminhao = str(input('''O caminhão está esperando carga? [S/N]
''')).strip().upper()


#Programa principal
while True:
    #Dados Trabalhador
    nome = str(input('Seu nome: '))
    usuario_senha = int(input('Senha[999 para sair]:  '))
    if usuario_senha == 999:
        print('Sistema encerrado')
        break
    while usuario_senha != senha:
        print('Senha inválida')
        usuario_senha = int(input('Senha[999 para sair]:  '))
    #Saudações
    print('olá!')
    sleep(0.5)
    print(f'Seja bem-vindo ao sistemas de cargas, {nome}!')
    sleep(0.5)
    #Inicio do sistema
    escolha = str(input('''Deseja iniciar o sistema? [S/N]
''')).upper().strip()[0]
    while escolha not in 'SN':
        escolha = str(input('''Deseja iniciar o sistema? [S/N]
''')).upper().strip()[0]
    if escolha == 'S':
        print('Iniciando sistema...')
        sleep(1)
        print(f'Sistema iniciado em {date.today()}')
        caminhao()
    if escolha == 'N':
        pergunta = int(input('''
[0] para iniciar o programa
[1] para sair
'''))
        if pergunta == 1:
            print('Programa encerrado')
            break
        if pergunta == 0:
            print('Iniciando sistema...')
            sleep(1)
            print(f'Sistema iniciado em {date.today()}')
            caminhao()
        while pergunta not in numero:
            pergunta = str(input('''
[0] para iniciar o programa
[1] para sair
'''))